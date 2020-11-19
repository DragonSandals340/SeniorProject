from gbAPI import __version__
from setuptools import setup, find_packages


setup(
    name='gbAPI',
    description='A REST API used for remote play chess.',
    version=__version__,
    author="Chris Webster",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gbAPI = gbAPI.gbAPI:main'
        ]
    },
)