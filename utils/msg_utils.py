from utils.decorators import delayed


def message_stat(api, chat_id, start=0, nmessages=2000):

	stats = dict()

	for offset in range(start, nmessages, 200):

		chat_slice = delayed()(api.messages.getHistory)(chat_id=chat_id, count=200, offset=offset)

		for msg in chat_slice[1:]:
			uid = msg['uid']
			if uid in stats:
				stats[uid] += 1
			else:
				stats[uid] = 1

	return stats
