#!/usr/bin/env python3

import ats.senza

from setuptools import setup, find_packages

PROJECT = 'ats.senza'

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=ats.senza.version,

    description='Sensor event API and client for AiC VMs',
    long_description=long_description,

    author='AiC Project',
    author_email='aic-project@alterway.fr',

    install_requires=[
        'ats.client',

        # server
        'aiohttp',
        'aiohttp-debugtoolbar',
        'aioamqp',
        'jsonschema',
        'protobuf',
        'structlog',
        'ats.util',

        # development
        'pyflakes',     # supports async/await
    ],
    extras_require={
        'docs': (
            'sphinx',
            'sphinx_rtd_theme',
            'sphinxcontrib-httpdomain',
            'sphinxcontrib-seqdiag',
            'sphinxcontrib-programoutput',
        )},
    namespace_packages=['ats'],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'senza = ats.senza.client.app:main',
            'senza-server = ats.senza.server.main:main',
        ],
        # for Cliff
        'senza': [
            'schema = ats.senza.client.schema:Schema'
        ] + [
            '%s = ats.senza.client.commands.%s:Command' % (protocol, protocol.replace('-', '_'))
            for protocol in [
                'accelerometer',
                'battery',
                'camera',
                'gps',
                'gravity',
                'gyroscope',
                'light',
                'linear-acc',
                'magnetometer',
                'orientation',
                'pressure',
                'proximity',
                'recorder',
                'rotation-vector',
                'relative-humidity',
                'temperature',
            ]
        ] + [
            'gsm %s = ats.senza.client.commands.gsm.%s:Command' % (protocol, protocol.replace('-', '_'))
            for protocol in [
                'call',
                'sms',
                'signal',
                'network',
                'registration'
            ]
        ]
    },

    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-asyncio'],

    zip_safe=False,
)
