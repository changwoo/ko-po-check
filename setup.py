#!/usr/bin/env python

import sys
if sys.version_info.major < 3:
    print('This program is only for Python 3.x. Run with python3.')
    sys.exit(1)

from distutils.core import setup
from KPC.config import VERSION

setup(name='ko-po-check',
      version=VERSION,
      description='Korean PO checker',
      author='Changwoo Ryu',
      author_email='cwryu@debian.org',
      url='https://github.com/changwoo/ko-po-check',

      packages = ['KPC', 'KPC/checks',
                  'KPC/checks/language',
                  'KPC/checks/convention',
                  'KPC/checks/terminology' ],
      scripts=['scripts/ko-po-check'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' +
            'GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Localization',
        ],
      )
 
