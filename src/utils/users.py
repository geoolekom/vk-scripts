from utils.decorators import delayed
from utils.getters import get_data

MAX_USER_IDS = 100


def get_chat_names(api, chat_id):

	users = dict()
	user_list = delayed()(api.messages.getChatUsers)(chat_id=chat_id, fields=['first_name', ])

	for user in user_list:
		uid = user['uid']
		name = "{0} {1}".format(
			user['first_name'],
			user['last_name']
		)

		users[uid] = name

	return users


def get_name_by_id(api, user_id):
	user = delayed()(api.users.get)(user_id=user_id)

	if not user:
		raise ValueError('Нет пользователя с таким id.')
	else:
		user = user[0]

	name = "{0} {1}".format(
		user['first_name'],
		user['last_name']
	)
	return name


def get_names_by_ids(api, user_ids, user_dict=None):

	user_ids_filtered = [uid for uid in user_ids if uid not in user_dict]

	data_iter = [
		dict(','.join(user_ids[n: n + MAX_USER_IDS]))
		for n in range(0, len(user_ids_filtered), MAX_USER_IDS)
	]

	users = get_data(api, 'users.get', data_iter)
	return [
		"{0} {1}".format(
			user['first_name'],
			user['last_name']
		) for user in users
	]