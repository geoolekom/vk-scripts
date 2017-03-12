from utils.decorators import delayed
from utils.getters import get_data

MAX_USER_IDS = 100


def get_chat_names(api, chat_id):

	user_list = delayed()(api.messages.getChatUsers)(chat_id=chat_id, fields=['first_name', ])

	return {user['uid']: user for user in user_list}


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


def get_users(api, user_ids, user_dict=None):

	if not user_dict:
		user_ids_filtered = [uid for uid in user_ids if uid not in user_dict]
	else:
		user_ids_filtered = [uid for uid in user_ids]

	data_iter = [
		dict(
			user_ids=','.join(map(str, user_ids_filtered[n: n + MAX_USER_IDS]))
		) for n in range(0, len(user_ids_filtered), MAX_USER_IDS)
	]

	user_list = get_data(api, 'users.get', data_iter)
	new_user_dict = {
			user['uid']: user for user in user_list
		}

	if user_dict is None:
		return new_user_dict
	else:
		user_dict.update(new_user_dict)
		return user_dict


def get_full_names(user_dict):
	return {
		key: "{0} {1}".format(
			user['first_name'],
			user['last_name']
		) for key, user in user_dict.items()
	}
