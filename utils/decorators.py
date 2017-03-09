import time
import math

from vk.exceptions import VkAPIError


def delayed(delay=0.2):
	def decorator(func):
		def wrapper(*args, **kwargs):
			result = None
			error = None
			for _ in range(math.ceil(1.0/delay)):
				try:
					result = func(*args, **kwargs)
					break
				except VkAPIError as e:
					error = e
				finally:
					time.sleep(delay)
			if result:
				return result
			else:
				raise error

		return wrapper
	return decorator
