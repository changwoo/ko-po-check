#!/usr/bin/env python2.2

import os, sys, string

dir = os.path.dirname(sys.argv[0])
exe = "python " + dir + "/ko-po-check"
sys.exit(os.system(exe + " --moduledir=%s "% dir + string.join(sys.argv[1:],' ')))
