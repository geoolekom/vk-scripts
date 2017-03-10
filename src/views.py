import collections
import functools


def text_hist(labels, stats, rate=True):

	ordered_stats = collections.OrderedDict(
		sorted(
			stats.items(),
			key=lambda item: item[1]
		)
	)

	if stats.values():
		ndata = functools.reduce(
			lambda x, y: x + y,
			stats.values()
		)
	else:
		ndata = 0

	print(ndata)

	for uid in ordered_stats:
		name = labels[uid].ljust(40)
		if rate:
			value = round(stats[uid] / ndata * 100, 2)
		else:
			value = stats[uid]

		print("{0} {1}".format(name, value))
