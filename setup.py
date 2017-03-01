from setuptools import setup, find_packages
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-fullurl',
    version='0.1',
    packages=find_packages(exclude=['testproject']),
    author='David D Lowe',
    author_email='daviddlowe.flimm@gmail.com',
    description='The template tag `fullurl` acts just like `url`, but it always prints absolute URLs with scheme and domain',
    long_description=open(os.path.join(BASE_DIR, 'README.rst'), "rb").read().decode("UTF-8"),
    license='cc0',
    keywords=['django'],
    install_requires=[
        'Django>=1.10',
    ],
    url='https://github.com/Flimm/django-fullurl',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Programming Language :: Python :: 3.6',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    ],
)
