#!/usr/bin/env python

"""
test code for app module

can be run with py.test or nosetests
"""

def test_init():
    """ makes sure it imports and can be read"""
    import app
    assert hasattr(app, '__version__')

