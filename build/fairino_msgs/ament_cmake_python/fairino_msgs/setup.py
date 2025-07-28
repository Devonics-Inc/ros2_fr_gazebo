from setuptools import find_packages
from setuptools import setup

setup(
    name='fairino_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('fairino_msgs', 'fairino_msgs.*')),
)
