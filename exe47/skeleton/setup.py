try:
    from setuptools import setup 
except ImportError:
    from distutils.core import setup

config = {
    'description': 'qiaomuProject',
    'author': 'qiaomu',
    'url': '...',
    'download_url': '...',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages'; ['exe47'],
    'scripts': [],
    'name': 'qiaomuProject'
}

setup(**config)

