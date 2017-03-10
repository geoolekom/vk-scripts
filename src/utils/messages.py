from utils.getters import get_data


def get_messages(api, nmessages, per_request=200, start=0, **credentials):
	chat_slice = get_data(api, 'messages.getHistory', nmessages, per_request, start, **credentials)
	return chat_slice


def message_hist(api, message_handler_list, nmessages, **credentials):
	stats = [dict() for _ in message_handler_list]
	chat_slice = get_messages(api, nmessages=nmessages, **credentials)

	for i, handler in enumerate(message_handler_list):
		for msg in chat_slice:
			handler(stats[i], msg)

	return stats
