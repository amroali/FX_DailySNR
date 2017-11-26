try:
	from setuptools import setup 
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Forex Daily Stop and Reverse Strategy',
	'author': 'Amro Ali',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'theamroali@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'FX_DailySNR'
}

setup(**config)