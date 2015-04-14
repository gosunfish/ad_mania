#!/usr/bin/env python

from setuptools import setup

import ad_mania # to get __version__

setup(
    name='ad_mania',
    version = ad_mania.__version__,
    author='Carolyn Evans',
    author_email='gosunfish@comcast.net',
    packages = ['ad_mania', 'ad_mania/test'],
    url='https://github.com/gosunfish/ad_mania',
    description='Ad Server',
    long_description=open('README.rst').read(),
    license=open('LICENSE.txt').read(),
    install_requires=[
        'pytest',
        'requests'],)


