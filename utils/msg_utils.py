from utils.decorators import delayed

import itertools
import json


def message_stat(api, chat_id, start=0, nmessages=2000, per_connect=5000, per_request=200):

	stats = dict()

	count, start_message = delayed()(api.messages.getHistory)(chat_id=chat_id, count=1)
	limit_all = min(nmessages, count)
	limit_connect = min(nmessages, per_connect)
	limit_request = min(nmessages, per_request)

	for offset in range(start, limit_all, per_connect):

		method_call_list = list()

		for i in range(0, limit_connect, per_request):
			method_call_list.append(
				'API.messages.getHistory({0}).slice(1)'.format(
					json.dumps(dict(chat_id=chat_id, count=limit_request, offset=offset+i))
				)
			)

		response = delayed()(api.execute)(
			code='return [{0}];'.format(
				', '.join(method_call_list)
			)
		)

		chat_slice = list(itertools.chain.from_iterable(response))

		for msg in chat_slice:
			uid = msg['uid']
			if uid in stats:
				stats[uid] += 1
			else:
				stats[uid] = 1

	return stats
