client_id = 5913330

redirect_uri = 'https://oauth.vk.com/blank.html'

display = 'page'

scope = [
	'friends',
	'messages',
	'wall',
]

response_type = 'token'

v = 5.62

get_data = dict(
	client_id=client_id,
	redirect_uri=redirect_uri,
	display=display,
	scope=','.join(scope),
	response_type=response_type,
	v=v
)
