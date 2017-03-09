import collections
import vk

import auth
import utils
import views

result = auth.get_auth_data()

token = result['access_token']
traced_user_id = result['user_id']

session = vk.Session(access_token=token)
api = vk.API(session=session)

chat_id = 100
nmessages = 1000000
users = utils.get_chat_names(api, chat_id)
stats = utils.message_stat(api, chat_id, nmessages=nmessages)
deleted_users = [uid for uid in stats if uid not in users]

for uid in deleted_users:
	users[uid] = utils.get_name_by_id(api, uid)

views.message_rate(users, stats, nmessages)

