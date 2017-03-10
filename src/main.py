import vk

import auth
import utils
import views
import handlers

result = auth.get_auth_data()
token = result['access_token']

session = vk.Session(access_token=token)
api = vk.API(session=session)


def messages_script():

	chat_id = 100
	nmessages = 1000

	users = utils.get_chat_names(api, chat_id)

	messages = utils.get_messages(
		api,
		chat_id=chat_id,
		nmessages=nmessages
	)

	msg_stats = utils.data_to_hist(
		handler=handlers.message_count_handler,
		data=messages
	)

	deleted_users = [uid for uid in msg_stats if uid not in users]

	for uid in deleted_users:
		users[uid] = utils.get_name_by_id(api, uid)

	views.text_hist(
		labels=users,
		stats=msg_stats,
		rate=True
	)


def post_script():

	posts = utils.get_wall_posts(
		api,
		owner_id=-30602036,
		nposts=1000
	)

	post_stats = utils.data_to_hist(
		data=posts,
		handler=handlers.post_like_handler
	)

	views.text_hist(post_stats, rate=False)

messages_script()



