import vk
# import cProfile

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
	nmessages = 5000

	messages = utils.get_messages(
		api,
		chat_id=chat_id,
		# user_id=183824694,
		nmessages=nmessages
	)
	# [print(msg) for msg in messages]

	msg_stats, = utils.data_to_hist(
		handler_list=[handlers.word_mentioned_handler('светюха', 'кирилл', 'керил')],
		data=messages
	)

	users = utils.get_chat_names(api, chat_id)
	utils.get_users(api, user_ids=msg_stats, user_dict=users)

	names = utils.get_full_names(users)

	views.plot_view(
		labels=names,
		stats=msg_stats,
		order_by=lambda item: item[1],
		rate=False
	)


def post_script():

	posts = utils.get_wall_posts(
		api,
		owner_id=-30602036,
		nposts=1000
	)

	post_stats, = utils.data_to_hist(
		data=posts,
		handler_list=[handlers.post_like_handler]
	)

	views.text_hist(post_stats, rate=False)

messages_script()


