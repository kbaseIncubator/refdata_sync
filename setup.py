#!/usr/bin/env python
from distutils.core import setup

setup(
    name='refdata_sync',
    version='0.0.1',
    description='Sync genomic refdata to the local filesystem',
    author='KBase Team',
    author_email='info@kbase.us',
    url='https://github.com/kbaseincubator/refdata_sync',
    package_dir={'': 'src'},
    packages=['refdata_sync'],
    scripts=[
        'src/kbase_module/scripts/entrypoint.sh'
    ],
    install_requires=[],
    python_requires='>3'
)
