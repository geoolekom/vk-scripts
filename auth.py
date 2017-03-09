import requests
import browser_cookie3

import settings


def get_auth_data():

	cookies = browser_cookie3.load()

	response = requests.get(
		'https://oauth.vk.com/authorize',
		params=settings.get_data,
		cookies=cookies
	)

	result = requests.utils.urlparse(response.url).fragment

	if result:
		return dict([item.split('=') for item in result.split('&')])
	else:
		raise ConnectionError('Авторизация не произошла.')
