from setuptools import setup, find_packages
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

readme = open(os.path.join(BASE_DIR, 'README.rst'), 'rb').read().decode('UTF-8')
changelog = open(os.path.join(BASE_DIR, 'CHANGELOG.rst'), 'rb').read().decode('UTF-8')

setup(
    name='django-fullurl',
    version='0.4',
    packages=find_packages(exclude=['testproject']),
    author='David D Lowe',
    author_email='daviddlowe.flimm@gmail.com',
    description='The template tag `fullurl` acts just like `url`, but it always prints absolute URLs with scheme and domain',
    long_description=readme + '\n\n' + changelog,
    license='mit',
    keywords=['django'],
    install_requires=[
        'Django>=1.8',
    ],
    url='https://github.com/Flimm/django-fullurl',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)
