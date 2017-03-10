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
nmessages = 100000
users = utils.get_chat_names(api, chat_id)
word_stats, word_count_stats = utils.message_hist(
	api,
	chat_id=chat_id,
	nmessages=nmessages,
	message_handler_list=[
		handlers.word_mentioned_handler('заказчик', 'заказчика', 'заказчику'),
		handlers.word_count_handler
	]
)

deleted_users = [uid for uid in word_count_stats if uid not in users or uid not in word_stats]

for uid in deleted_users:
	users[uid] = utils.get_name_by_id(api, uid)
	word_stats[uid] = 0

views.message_rate(
	users,
	word_stats,
	rate=True)

