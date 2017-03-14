import functools
import plotly


def dict_view(view_method, keys, data_dict, label_dict=None, rate=False):
	if not keys:
		print('Нечего выводить!')
		return

	ndata = functools.reduce(
		lambda x, y: x + y,
		[data_dict[key] for key in keys]
	)

	if not label_dict:
		labels = [str(key).ljust(40) for key in keys]
	else:
		labels = [str(label_dict[key]).ljust(40) for key in keys]

	if rate:
		values = [round(data_dict[key]/ndata, 2) for key in keys]
	else:
		values = [data_dict[key] for key in keys]

	view_method(labels, values)

	print("Всего: {0}".format(ndata))


def text_hist(labels, values):

	for i in range(len(labels)):
		print("{0} {1}".format(labels[i], values[i]))

	# print(map("{0} {1}".format, labels, values))


def plotly_hist(labels, values):

	plotly.offline.plot(
		{
			'data': [plotly.graph_objs.Bar(
				x=labels,
				y=values,
				# orientation='h'
			)],
			'layout': plotly.graph_objs.Layout(margin=dict(l=150)),
		},
		filename='../chart.html'
	)


