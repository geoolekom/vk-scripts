import vk

import auth
import utils
import views
import handlers

result = auth.get_auth_data()
token = result['access_token']

session = vk.Session(access_token=token)
api = vk.API(session=session)

chat_id = 100
nmessages = 1000

posts = utils.get_wall_posts(
	api,
	owner_id=-30602036,
	nposts=100
)

users = utils.get_chat_names(api, chat_id)

messages = utils.get_messages(
	api,
	chat_id=chat_id,
	nmessages=nmessages
)

word_stats, word_count_stats = utils.data_to_hist(
	handler_list=[
		handlers.word_mentioned_handler('заказчик', 'заказчика', 'заказчику'),
		handlers.word_count_handler
	],
	data=messages
)

deleted_users = [uid for uid in word_count_stats if uid not in users or uid not in word_stats]

for uid in deleted_users:
	users[uid] = utils.get_name_by_id(api, uid)
	word_stats[uid] = 0

views.text_hist(
	users,
	word_stats,
	rate=True)

