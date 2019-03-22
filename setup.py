from setuptools import setup, find_packages
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

readme = open(os.path.join(BASE_DIR, 'README.rst'), 'rb').read().decode('UTF-8')
changelog = open(os.path.join(BASE_DIR, 'CHANGELOG.rst'), 'rb').read().decode('UTF-8')

setup(
    name='django-fullurl',
    version='1.0',
    packages=find_packages(exclude=['testproject']),
    author='David D Lowe',
    author_email='daviddlowe.flimm@gmail.com',
    description='Adds three template tags to Django: `fullurl`, `fullstatic` and `buildfullurl`. The template tag `fullurl` acts just like `url`, but it always prints absolute URLs with scheme and domain',
    long_description=readme + '\n\n' + changelog,
    long_description_content_type='text/x-rst',
    license='mit',
    keywords=['django'],
    install_requires=[
        'Django>=1.8',
    ],
    project_urls={
        'GitHub': 'https://github.com/Flimm/django-fullurl',
        'Change log': 'https://github.com/Flimm/django-fullurl/blob/master/CHANGELOG.rst',
        'Say Thanks!': 'https://saythanks.io/to/Flimm',
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
