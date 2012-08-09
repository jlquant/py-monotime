#!/usr/bin/env python
from distutils.core import setup, Extension

_mod = Extension('_monotime', sources=['_monotime.c'], libraries=['rt'])

setup(
    name='Monotime',
    version='1.0',
    description='time.monotonic() for older python versions',
    author='Avery Pennarun',
    author_email='apenwarr@google.com',
    url='TODO',
    packages=['monotime'],
    ext_modules=[_mod],
    package_dir={'monotime': ''},
)
