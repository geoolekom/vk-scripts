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


def hui_finder(stats, message):
	uid = message['uid']
	words = [word.lower() for word in message['body'].split(' ')]
	if 'хуй' in words:
		if uid in stats:
			stats[uid] += 1
		else:
			stats[uid] = 1
