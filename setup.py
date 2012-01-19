#!/usr/bin/env python

"""
@file setup.py
@see http://peak.telecommunity.com/DevCenter/setuptools
"""

import sys
import os

# Add /usr/local/include to the path for macs, fixes easy_install for several packages (like gevent and pyyaml)
if sys.platform == 'darwin':
    os.environ['C_INCLUDE_PATH'] = '/usr/local/include'

setupdict = {
    'name' : 'epuharness',
    'version' : '0.1.0',
    'description' : 'OOICI CEI Elastic Processing Unit Test Harness',
    'url': 'https://confluence.oceanobservatories.org/display/CIDev/Common+Execution+Infrastructure+Development',
    'download_url' : 'http://ooici.net/packages',
    'license' : 'Apache 2.0',
    'author' : 'CEI',
    'author_email' : 'patricka@uvic.ca',
    'keywords': ['ooici','cei','epu'],
    'classifiers' : [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering'],
}

from setuptools import setup, find_packages
setupdict['packages'] = find_packages()

setupdict['dependency_links'] = ['http://ooici.net/releases']
setupdict['test_suite'] = 'epuharness'

# ssl package won't install on 2.6+, but is required otherwise.
# also, somehow the order matters and ssl needs to be before ioncore
# in this list (at least with setuptools 0.6c11).

setupdict['install_requires'] = []
if sys.version_info < (2, 6, 0):
    setupdict['install_requires'].append('ssl==1.15-p1')

setupdict['install_requires'] += ['pyyaml',
                                  'dashi==0.1',
                                  'gevent==0.13.6',
                                  'pidantic',
                                  'nose',
                                 ]
setupdict['tests_require'] = ['nose']
setupdict['test_suite'] = 'nose.collector'

setupdict['entry_points'] = {
        'console_scripts': [
            'epu-harness=epuharness.cli:main',
            ]
        }

setupdict['package_data'] = {'epuharness': ['config/*.yml']}

setup(**setupdict)
