import os
import sys

import gpsimy

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
    pass

packages = [
    'gpsimy'
]

requires = []
setup(
    name='gpsimy',
    version=gpsimy.__version__,
    description='GPS Position and tracker abstraction',
    long_description=open('README.txt').read(),
    author='Gamaliel Espinoza Macedo',
    author_email='gamaliel.espinoza@gmail.com',
    url='https://github.com/gamikun/gpsimy',
    packages=packages,
    package_dir={'gpsimy': 'gpsimy'},
    install_requires=requires,
    include_package_data=True,
    package_data={},
    ext_modules=[],
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ),
)