#! /usr/bin/env python

import os, sys, string

dir = os.path.dirname(sys.argv[0])
exe = dir + "/ko-po-check"
sys.exit(os.system(exe + " --moduledir=%s "% dir + string.join(sys.argv[1:],' ')))
