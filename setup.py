#!/usr/bin/env python

import os
from codecs import open

from setuptools import find_packages, setup

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'pysigep',
                            '__version__.py')

about = {}
with open(version_path, 'r') as f:
    exec(f.read(), about)

with open('README.rst', 'r') as readme_file:
    readme = readme_file.read()

with open('docs/history.rst', 'r') as history_file:
    history = history_file.read()

requirements = [
    'zeep',
]

test_requirements = [
    'coveralls',
    'flake8',
]

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Natural Language :: Portuguese',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme + '\n\n' + history,
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__maintainer__'],
    maintainer_email=about['__maintainer_email__'],
    url=about['__url__'],
    download_url=about['__download_url__'],
    packages=find_packages(include=['pysigep']),
    package_dir={'pysigep': 'pysigep'},
    include_package_data=True,
    install_requires=requirements,
    license=about['__license__'],
    zip_safe=False,
    keywords='correios sigep sigepweb development api',
    classifiers=classifiers,
    platforms=['any'],
    test_suite='tests',
    tests_require=test_requirements,
)
