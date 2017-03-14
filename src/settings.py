from configparser import ConfigParser
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

config = ConfigParser()
config.read(
	os.path.join(PROJECT_DIR, '../vk.conf')
)

AUTH_DATA = {
	'client_id': config.get('auth', 'APP_ID'),
	'redirect_uri': config.get('auth', 'REDIRECT_URI'),
	'scope': config.get('auth', 'ACCESS_TO'),
	'display': 'page',
	'response_type': 'token',
	'v': 5.62,
}
