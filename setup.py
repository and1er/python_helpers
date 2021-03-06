#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'invoke>=1.0.0']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Andrei Losenkov",
    author_email='andrei.losenkov@outlook.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Helpers contains reusable functions for routine automation.",  # noqa: E501
    entry_points={
        'console_scripts': [
            'python_helpers=python_helpers.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='python_helpers',
    name='python_helpers',
    packages=find_packages(include=['python_helpers']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/and1er/python_helpers',
    version='0.3.3',
    zip_safe=False,
)
