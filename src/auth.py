import requests
import browser_cookie3
import webbrowser

import settings


def cookies_auth():

	cookies = browser_cookie3.load()

	response = requests.get(
		'https://oauth.vk.com/authorize',
		params=settings.AUTH_DATA,
		cookies=cookies
	)

	result = requests.utils.urlparse(response.url).fragment

	if result:
		return dict([item.split('=') for item in result.split('&')])
	else:
		webbrowser.get().open(response.url)
		raise ConnectionError('Авторизация не произошла.')

