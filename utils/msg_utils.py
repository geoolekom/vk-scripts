from utils.decorators import delayed

import itertools
import json


def get_messages(api, nmessages, start=0, per_connect=5000, per_request=200, **credentials):
	chat_slice = list()
	count, start_message = delayed()(api.messages.getHistory)(**credentials, count=1)

	limit_all = min(nmessages, count)
	limit_connect = min(nmessages, per_connect)
	limit_request = min(nmessages, per_request)

	for offset in range(start, limit_all, per_connect):

		method_call_list = list()

		for i in range(0, limit_connect, per_request):
			method_call_list.append(
				'API.messages.getHistory({0}).slice(1)'.format(
					json.dumps(dict(**credentials, count=limit_request, offset=offset+i))
				)
			)

		response = delayed()(api.execute)(
			code='return [{0}];'.format(
				', '.join(method_call_list)
			)
		)

		chat_slice += list(itertools.chain.from_iterable(response))

	return chat_slice


def message_hist(api, chat_id, message_handler_list, nmessages):

	stats = [dict() for _ in message_handler_list]
	chat_slice = get_messages(api, chat_id=chat_id, nmessages=nmessages)

	for i, handler in enumerate(message_handler_list):
		for msg in chat_slice:
			handler(stats[i], msg)

	return stats
