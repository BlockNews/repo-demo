#!/usr/bin/env python

from os.path import exists, join
from setuptools import setup, find_packages
import os
import platform
from sphinx.setup_command import BuildDoc

cmdclass = {'build_sphinx': BuildDoc}

#SCRIPTS =[]
SCRIPTS = [join('bin', s) for s in ['repo-demo']]

if os.name == "nt":
    SCRIPTS = [s+'.bat' for s in SCRIPTS]
elif os.name == "posix":
    SCRIPTS = [s + '.sh' for s in SCRIPTS]

setup(
    name='repo-demo',
    version=open('VERSION').read().strip(),
    author='David Koo',
    author_email='nuanguang.gu@aliyun.com',
    packages=find_packages(),
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', 'repo-demo'),
            'version': ('setup.py', open('VERSION').read().strip()),
            'release': ('setup.py', open('VERSION').read().strip()),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', 'docs/build'),
        }
    },
    scripts=SCRIPTS,
    url='https://github.com/BlockNews/repo-demo',
    license='BlockNews Reserved',
    description='repo-demo',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    #use_2to3=True,
    #convert_2to3_doctests=['README.md'],
    #converter_2to3_fixers=[],
    include_package_data=True,
    # Any requirements here
    install_requires=[
        'requests',
        'wheel',
        'setuptools',
        'geoip2',
        'psutil',
        'numpy',
        'PySocks',
        'Sphinx',
        'idata-security>=1.0.1',
        'ifits-utils>=1.0.1',
        'ifits-aws>=1.0.17',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
)