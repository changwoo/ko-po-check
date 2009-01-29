#!/usr/bin/env python
from distutils.core import setup
from KPC.config import VERSION

setup(name='ko-po-check',
      version=VERSION,
      description='Korean PO checker',
      author='Changwoo Ryu',
      author_email='cwryu@debian.org',
      url='http://kldp.net/projects/ko-po-check',

      packages = ['KPC', 'KPC/checks',
                  'KPC/checks/language',
                  'KPC/checks/convention',
                  'KPC/checks/terminology' ],
      scripts=['scripts/ko-po-check'],
      )
 
