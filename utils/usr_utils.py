from utils.decorators import delayed


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
