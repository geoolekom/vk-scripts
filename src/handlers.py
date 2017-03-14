import string
import datetime


def user_messages_count(stats, message):
	uid = message['uid']
	if uid in stats:
		stats[uid] += 1
	else:
		stats[uid] = 1


def user_messages_length(stats, message):
	uid = message['uid']
	if uid in stats:
		stats[uid] += len(message['body'])
	else:
		stats[uid] = len(message['body'])


def daily_messages(stats, message):
	date = datetime.date.fromtimestamp(message['date'])
	if date in stats:
		stats[date] += 1
	else:
		stats[date] = 1


def user_stickers(stats, message):
	uid = message['uid']
	if 'attachment' in message and message['attachment']['type'] == 'sticker':
		if uid in stats:
			stats[uid] += 1
		else:
			stats[uid] = 1


def user_words_mentioned(*tokens):
	def handler(stats, message):
		token_set = set(tokens)
		uid = message['uid']
		words = [word.lower() for word in message['body'].split(' ')]
		words = [word.translate(word.maketrans('', '', string.punctuation)) for word in words if word]
		if len(token_set.intersection(set(words))):
			if uid in stats:
				stats[uid] += 1
			else:
				stats[uid] = 1
	return handler


def user_words_count(stats, message):
	uid = message['uid']
	nwords = len(message['body'].split())
	if uid in stats:
		stats[uid] += nwords
	else:
		stats[uid] = nwords


def word_popularity(stats, message):
	text = message['body'].translate(
		message['body'].maketrans('', '', string.punctuation)
	)
	words = [word.lower() for word in text.split(' ') if word]
	words = [word for word in words if len(word) > 4]

	for word in words:
		if word in stats:
			stats[word] += 1
		else:
			stats[word] = 1


def user_audio_messages(stats, message):
	uid = message['uid']
	if not message['body'] and 'attachments' in message:
		att_list = message['attachments']
		for att in att_list:
			if att['type'] == 'doc' and 'ext' in att['doc'] and att['doc']['ext'] == 'ogg':
				if uid in stats:
					stats[uid] += 1
				else:
					stats[uid] = 1


def post_likes(stats, post):
	pid = post['id']
	nlikes = post['likes']['count']

	if pid in stats:
		stats[pid] += nlikes
	else:
		stats[pid] = nlikes


def daily_posts(stats, post):
	date = datetime.date.fromtimestamp(post['date'])
	if date in stats:
		stats[date] += 1
	else:
		stats[date] = 1


def daily_likes(stats, post):
	date = datetime.date.fromtimestamp(post['date'])
	if date in stats:
		stats[date] += post['likes']['count']
	else:
		stats[date] = post['likes']['count']

