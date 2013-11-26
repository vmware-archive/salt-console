#!/usr/bin/env python
'''
The setup script for salt console
'''

import os
# Use setuptools only if the user opts-in by setting the USE_SETUPTOOLS env var
# This ensures consistent behavior but allows for advanced usage with
# virtualenv, buildout, and others.
USE_SETUPTOOLS = False
if 'USE_SETUPTOOLS' in os.environ:
    try:
        from setuptools import setup
        USE_SETUPTOOLS = True
    except:
        USE_SETUPTOOLS = False


if USE_SETUPTOOLS is False:
    from distutils.core import setup


# pylint: disable-msg=W0122,E0602
exec(compile(open('sconsole/version.py').read(), 'sconsole/version.py', 'exec'))
VERSION = __version__
# pylint: enable-msg=W0122,E0602

NAME = 'salt-console'
DESC = ('A curses console interface to view Salt jobs')

kwargs = {}

kwargs.update(
    name=NAME,
    version=VERSION,
    description=DESC,
    author='Thomas S Hatch',
    author_email='thatch@saltstack.com',
    url='http://saltstack.org',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        ],
    packages=['sconsole'],
    scripts=['scripts/salt-console'],
)

if USE_SETUPTOOLS:
    kwargs.update(
        install_requires=open('requirements.txt').readlines(),
    )

setup(**kwargs)
