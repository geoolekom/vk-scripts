import string


def message_count_handler(stats, message):
	uid = message['uid']
	if uid in stats:
		stats[uid] += 1
	else:
		stats[uid] = 1


def message_length_handler(stats, message):
	uid = message['uid']
	if uid in stats:
		stats[uid] += len(message['body'])
	else:
		stats[uid] = len(message['body'])


def sticker_handler(stats, message):
	uid = message['uid']
	if 'attachment' in message and message['attachment']['type'] == 'sticker':
		if uid in stats:
			stats[uid] += 1
		else:
			stats[uid] = 1


def word_mentioned_handler(*tokens):
	def handler(stats, message):
		token_set = set(tokens)
		uid = message['uid']
		words = [word.lower() for word in message['body'].split(' ')]
		words = [word.translate(word.maketrans('', '', string.punctuation)) for word in words]
		if len(token_set.intersection(set(words))):
			if uid in stats:
				stats[uid] += 1
			else:
				stats[uid] = 1
	return handler


def word_count_handler(stats, message):
	uid = message['uid']
	nwords = len(message['body'].split())
	if uid in stats:
		stats[uid] += nwords
	else:
		stats[uid] = nwords
