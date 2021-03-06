#!/usr/bin/env python
"""fdb package is a set of Firebird RDBMS bindings for python.
It works on Python 2.6+ and Python 3.x.

"""
import sys
from setuptools import setup, find_packages
from fdb_embedded import __version__
from setuptools.command.test import test as TestCommand
import build_firebird

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database',
]

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = []
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


setup(name='fdb_embedded',
    version=__version__,
    description = 'Firebird RDBMS bindings for Python with built in fb embedded server.',
    url = "https://github.com/andrewleech/fdb_embedded",
    classifiers=classifiers,
    keywords=['Firebird'],
    license='BSD',
    author='Andrew Leech',
    author_email='andrew@alelec.net',
    long_description=__doc__,
    install_requires=['requests'],
    setup_requires=[],
    tests_require=['tox'],
    cmdclass = {
        'test': Tox,
        'build_ext': build_firebird.BuildFirebirdCommand,
    },
    ext_modules=build_firebird.ext_modules,
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=False,
    package_data={'fdb_embedded': ['*.txt'],
                  'test':'fbtest.fdb'},

    zip_safe=False,
    platforms=['Win32', 'Win64', 'Linux x86', 'Linux AMD64', 'Mac OS X x86_64']
)
