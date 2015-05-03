#!/usr/bin/env python

from setuptools import setup

import run # to get __version__

setup(
    name='ad_mania.py',
    version = run.__version__,
    author='Carolyn Evans',
    author_email='gosunfish@comcast.net',
    packages = ['ad_mania.py', 'ad_mania.py/test'],
    url='https://github.com/gosunfish/ad_mania.py',
    description='Ad Server',
    long_description=open('README.rst').read(),
    license=open('LICENSE.txt').read(),
    install_requires=[
        'requests',
        'uwsgi'],)


