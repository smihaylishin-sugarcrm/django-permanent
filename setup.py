#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

tests_require = ["Django>=1.7.0"]

try:
    import django
    if django.VERSION < (1, 7, 0):
        tests_require.append("django-model-utils==2.3.1")

except ImportError:
    pass

setup(
    name='django-permanent',
    version='1.1.9',
    description='Yet another approach to provide soft (logical) delete or masking (thrashing) django models instead of deleting them physically from db.',
    author='Mikhail Antonov',
    author_email='atin65536@gmail.com',
    long_description=open('README.rst').read(),
    url='https://github.com/MnogoByte/django-permanent',
    packages=find_packages(),
    install_requires=["Django>=1.6.0"],
    keywords=['django', 'delete', 'undelete', 'safedelete', 'remove', 'restore', 'softdelete', 'logicaldelete', 'trash'],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
    ],
    tests_require=tests_require,
    test_suite='runtests.runtests',
    license="BSD"
)
