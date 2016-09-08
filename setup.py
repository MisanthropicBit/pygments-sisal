"""pygments-sisal module setup script for distribution."""

from __future__ import with_statement

import os
import distutils.core


def get_version(filename):
    with open(filename) as fh:
        for line in fh:
            if line.startswith('__version__'):
                return line.split('=')[-1].strip()[1:-1]


distutils.core.setup(
    name='pygments-sisal',
    version=get_version(os.path.join('pygments-sisal', '__init__.py')),
    author='Alexander Asp Bock',
    author_email='alexander.asp.bock@gmail.com',
    platforms='All',
    description=('A pygments lexer for SISAL'),
    license='MIT',
    keywords='pygments, lexer, sisal',
    url='https://github.com/MisanthropicBit/pygments-sisal',
    packages=['pygments-sisal'],
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Terminals',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    # Pygments entry point
    entry_points="[pygments.lexers]"
                 "sisal=pygments-sisal:SisalLexer"
)
