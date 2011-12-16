#!/usr/bin/env python

from distutils.core import setup

from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup(name = 'pyuca',
      version = '1.0',
      description = 'Python Unicode Collation Algorithm (originally developed by James Tauber)',
      long_description=open("README.md").read(),
      author = 'Denis Krienb\xc3\xbchl',
      author_email = 'denis.krienbuehl@gmail.com',
      url = 'https://github.com/href/Python-Unicode-Collation-Algorithm',
      packages=['pyuca'],
      classifiers = [
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Topic :: Software Development :: Internationalization'
         ],
      #scripts = ['path/to/script']
  )
