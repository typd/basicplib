#!/usr/bin/env python
from setuptools import setup, find_packages

import basicplib

setup(
        name='basicplib',
        version=basicplib.__version__,
        description='basic python lib',
        long_description='basic python lib',
        author='yizhe',
        author_email='othertang@gmail.com',
        maintainer='yizhe',
        maintainer_email='othertang@gmail.com',
        platforms='any',
        license='GPL',
        packages=find_packages(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules' ]
)
