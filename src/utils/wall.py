from utils.getters import get_data


def get_wall_posts(api, nposts, per_request=100, start=0, **credentials):
	wall_slice = get_data(api, 'wall.get', nposts, per_request, start, **credentials)
	return wall_slice

