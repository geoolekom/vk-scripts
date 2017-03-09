import collections


def message_rate(users, stats, nmessages):

	ordered_stats = collections.OrderedDict(
		sorted(
			stats.items(),
			key=lambda item: item[1]
		)
	)

	for uid in ordered_stats:
		name = users[uid].ljust(40)
		rate = round(stats[uid] / nmessages * 100, 2)

		print("{0} {1}".format(name, rate))
