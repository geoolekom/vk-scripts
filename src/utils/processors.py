def data_to_hist(handler, data):
	stats = dict()
	[handler(stats, elem) for elem in data]
	# map(lambda elem: handler(stats, elem), data)
	return stats
