#!/usr/bin/env python

from setuptools import setup

import app # to get __version__

setup(
    name='app',
    version = app.__version__,
    author='Carolyn Evans',
    author_email='gosunfish@comcast.net',
    packages = ['app', 'app/test'],
    url='https://github.com/gosunfish/app',
    description='Ad Server',
    long_description=open('README.rst').read(),
    license=open('LICENSE.txt').read(),
    install_requires=[
        'pytest',
        'requests'],)


