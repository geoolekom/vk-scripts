import itertools


def data_to_hist(handler_list, data):
	stats_list = [dict() for _ in handler_list]

	[handler(stats, elem) for (handler, stats), elem in itertools.product(zip(handler_list, stats_list), data)]

	# map(
	# 	lambda handler, stats: map(lambda elem: handler(stats, elem), data),
	#   zip(handler_list, stats_list)
	# )
	return stats_list
