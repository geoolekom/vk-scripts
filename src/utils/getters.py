import itertools
import json

from utils.decorators import delayed
from vk.exceptions import VkAPIError

MAX_EXECUTE_QUERIES = 25


def execute(api, method_name, data_iter, handle=''):
	method_call_list = list()

	if len(data_iter) > MAX_EXECUTE_QUERIES:
		raise VkAPIError('Too many requests in one execute!')

	for data in data_iter:
		method_call_list.append(
			'API.{0}({1}){2}'.format(
				method_name,
				json.dumps(data),
				handle
			)
		)

	response = delayed()(api.execute)(
		code='return [{0}];'.format(
			', '.join(method_call_list)
		)
	)

	return list(itertools.chain.from_iterable(response))


def get_data(api, method_name, data_iter, handle=''):

	data_slice = list()

	for n in range(0, len(data_iter), MAX_EXECUTE_QUERIES):
		response = execute(api, method_name, data_iter[n:n + MAX_EXECUTE_QUERIES], handle)
		data_slice += response

	return data_slice

