# -*- coding: utf-8 -*-
"""
Emmett-Haml
-----------

This extension make it possible to use a
`haml <http://haml-lang.com/>`_ syntax in Emmett.
"""

import re

from setuptools import find_packages, setup

with open('emmett_haml/__init__.py', 'r', encoding='utf8') as f:
    version = re.search(r'__version__ = "(.*?)"', f.read(), re.M).group(1)


setup(
    name='Emmett-Haml',
    version=version,
    url='http://github.com/gi0baro/emmett-haml',
    license='BSD-3-Clause',
    author='Giovanni Barillari',
    author_email='gi0baro@d4net.org',
    description='Haml syntax for Emmett templates',
    long_description=__doc__,
    packages=find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=[
        'emmett',
        'renoir-haml'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    entry_points={}
)
