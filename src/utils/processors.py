def data_to_hist(handler_list, data):
	stats_list = [dict() for _ in handler_list]

	for handler, stats in zip(handler_list, stats_list):
		[handler(stats, elem) for elem in data]

	# map(
	# 	lambda handler, stats: map(lambda elem: handler(stats, elem), data),
	#   zip(handler_list, stats_list)
	# )
	return stats_list
