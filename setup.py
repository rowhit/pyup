#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "requests",
    "pygithub>=1.35",
    "click",
    "tqdm",
    "pyyaml",
    "packaging",
    "six",
    "python-gitlab>=1.3.0",
    "dparse>=0.4",
    "safety",
    "jinja2>=2.3"
]

test_requirements = [
    "requests-mock",
    "mock",
    "flake8"
]

setup(
    name='pyupio',
    version='1.0.2',
    description="A tool to update all your projects requirements",
    long_description=readme + '\n\n' + history,
    author="Jannis Gebauer",
    author_email='jay@pyup.io',
    url='https://github.com/pyupio/pyup',
    packages=[
        'pyup',
        'pyup.providers'
    ],
    package_dir={'pyup':
                 'pyup'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pyup',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
        'console_scripts': [
            'pyup = pyup.cli:main',
        ]
    },
    test_suite='tests',
    tests_require=test_requirements,
)
