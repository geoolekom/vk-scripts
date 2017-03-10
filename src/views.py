import collections
import functools


def message_rate(users, stats, rate=True):

	ordered_stats = collections.OrderedDict(
		sorted(
			stats.items(),
			key=lambda item: item[1]
		)
	)

	if stats.values():
		nmessages = functools.reduce(
			lambda x, y: x + y,
			stats.values()
		)
	else:
		nmessages = 0

	print(nmessages)

	for uid in ordered_stats:
		name = users[uid].ljust(40)
		if rate:
			value = round(stats[uid] / nmessages * 100, 2)
		else:
			value = stats[uid]

		print("{0} {1}".format(name, value))
