import collections
import functools


def text_hist(stats, labels=None, rate=False):

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

	for key in ordered_stats:

		if not labels:
			name = str(key).ljust(25)
		else:
			name = labels[key].ljust(40)

		if rate:
			value = round(stats[key] / ndata * 100, 2)
		else:
			value = stats[key]

		print("{0} {1}".format(name, value))

	print(ndata)
