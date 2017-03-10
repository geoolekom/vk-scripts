import itertools
import json

from utils.decorators import delayed


def get_data(api, method_name, ndata, per_request, start=0, **credentials):
	per_connect = 25*per_request
	data_slice = list()
	count, first_obj = delayed()(getattr(api, method_name))(**credentials, count=1)

	limit_all = min(ndata, count)

	for offset in range(start, limit_all, per_connect):

		method_call_list = list()
		limit_connect = min(limit_all - offset, per_connect)

		for i in range(0, limit_connect, per_request):
			limit_request = min(limit_connect - i, per_request)
			method_call_list.append(
				'API.{0}({1}).slice(1)'.format(
					method_name,
					json.dumps(dict(**credentials, count=limit_request, offset=offset + i))
				)
			)

		response = delayed()(api.execute)(
			code='return [{0}];'.format(
				', '.join(method_call_list)
			)
		)

		data_slice += list(itertools.chain.from_iterable(response))

	return data_slice