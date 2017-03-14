import vk
# import cProfile

import auth
import utils
import views
import handlers

result = auth.cookies_auth()
token = result['access_token']

session = vk.Session(access_token=token)
api = vk.API(session=session)


def messages_script():

	chat_id = 100
	nmessages = 3000

	messages = utils.get_messages(
		api,
		chat_id=chat_id,
		nmessages=nmessages
	)

	msg_stats, = utils.data_to_dict(
		handler_list=[handlers.user_messages_count],
		data=messages
	)

	users = utils.get_chat_users(api, chat_id)
	utils.get_users(api, user_ids=msg_stats, user_dict=users)

	names = utils.get_full_names(users)

	views.dict_view(
		view_method=views.plotly_hist,
		keys=sorted(
			list(msg_stats.keys()),
			key=lambda item: msg_stats[item]
		),
		label_dict=names,
		data_dict=msg_stats,
		rate=False
	)


def post_script():

	igm_id = -30602036
	plum_id = -50177168

	posts = utils.get_wall_posts(
		api,
		owner_id=igm_id,
		nposts=1000
	)

	daily_likes, daily_posts = utils.data_to_dict(
		data=posts,
		handler_list=[handlers.daily_likes, handlers.daily_posts]
	)

	views.dict_view(
		view_method=views.plotly_hist,
		keys=daily_likes.keys(),
		data_dict={
			key: daily_likes[key]/daily_posts[key] for key in daily_likes
		}
	)

post_script()


