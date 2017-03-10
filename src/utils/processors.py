def data_to_hist(handler_list, data):
	stats = [dict() for _ in handler_list]

	for i, handler in enumerate(handler_list):
		for elem in data:
			handler(stats[i], elem)

	return stats
