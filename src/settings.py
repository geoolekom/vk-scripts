from configparser import ConfigParser
import os

SOURCES_ROOT = os.path.dirname(os.path.abspath(__file__))

config = ConfigParser()
config.read(
	os.path.join(SOURCES_ROOT, '../vk.conf')
)

AUTH_DATA = {
	'client_id': config.get('auth', 'APP_ID'),
	'redirect_uri': 'https://oauth.vk.com/blank.html',
	'scope': config.get('auth', 'ACCESS_TO'),
	'display': 'page',
	'response_type': 'token',
	'v': 5.62,
}
