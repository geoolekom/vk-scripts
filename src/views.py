import collections
import functools
import plotly


def text_hist(keys, data_dict, label_dict=None, rate=False):

	if not keys:
		print('Нечего выводить!')
		return

	ndata = functools.reduce(
		lambda x, y: x + y,
		[data_dict[key] for key in keys]
	)

	if not label_dict:
		label_dict = {key: str(key) for key in keys}

	if rate:
		view_dict = {key: round(data_dict[key]/ndata, 2) for key in keys}
	else:
		view_dict = data_dict

	for key in keys:
		print("{0} {1}".format(
			label_dict[key].ljust(40),
			view_dict[key]
		))

	print("Всего: {0}".format(ndata))


def plot_hist(stats, labels=None, rate=False, order_by=lambda item: item[0]):

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
				x=x,
				y=y,
				# orientation='h'
			)],
			'layout': plotly.graph_objs.Layout(title="Message stats", margin=dict(l=150)),
		},
		filename='../chart.html'
	)


