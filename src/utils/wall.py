from utils.getters import get_data
from utils.decorators import delayed

MAX_POST_NUMBER = 100


def get_wall_posts(api, nposts, **credentials):

	count, first_obj = delayed()(api.wall.get)(**credentials, count=1)

	limit = min(count, nposts)

	data_iter = [
		dict(
			offset=offset,
			count=min(limit - offset, MAX_POST_NUMBER),
			**credentials
		) for offset in range(0, limit, MAX_POST_NUMBER)
	]

	wall_slice = get_data(api, 'wall.get', data_iter, handle='.slice(1)')
	return wall_slice

