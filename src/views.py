import collections
import functools
import plotly


def text_hist(stats, labels=None, rate=False, order_by=lambda item: item[0]):

	ordered_stats = collections.OrderedDict(
		sorted(
			stats.items(),
			key=order_by
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
			label = str(key).ljust(40)
		else:
			label = labels[key].ljust(40)

		if rate:
			value = round(stats[key] / ndata * 100, 2)
		else:
			value = stats[key]

		print("{0} {1}".format(label, value))

	print("Всего: {0}".format(ndata))


def plot_view(stats, labels=None, rate=False, order_by=lambda item: item[0]):

	ordered_stats = collections.OrderedDict(
		sorted(
			stats.items(),
			key=order_by
		)
	)

	if not labels:
		x = list(ordered_stats.keys())
	else:
		x = [labels[key] for key in ordered_stats]

	y = list(ordered_stats.values())

	plotly.offline.plot(
		{
			'data': [plotly.graph_objs.Bar(
				x=y[-30:],
				y=x[-30:],
				orientation='h'
			)],
			'layout': plotly.graph_objs.Layout(title="Message stats", margin=dict(l=150)),
		},
		filename='../chart.html'
	)


