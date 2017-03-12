from utils.getters import get_data
from utils.decorators import delayed

MAX_MESSAGES_NUMBER = 200


def get_messages(api, nmessages, **credentials):

	count, first_obj = delayed()(api.messages.getHistory)(**credentials, count=1)

	limit = min(count, nmessages)

	data_iter = [
		dict(
			offset=offset,
			count=min(limit - offset, MAX_MESSAGES_NUMBER),
			**credentials
		) for offset in range(0, limit, MAX_MESSAGES_NUMBER)
	]

	chat_slice = get_data(
		api,
		'messages.getHistory',
		data_iter,
		handle='.slice(1)'
	)

	return chat_slice
