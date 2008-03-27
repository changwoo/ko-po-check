# -*- coding: utf-8 -*-
import re, string

name = "convention/copyright"

copyright_re = re.compile(r"^([Cc]opyright )?\([Cc]\) ")

error_string = u'copyright notice는 번역하면 안 됩니다'

def check(msgid,msgstr):
    msgid_lines = string.split(msgid,"\n")
    msgstr_lines = string.split(msgstr,"\n")
    lineno = 0
    for line in msgid_lines:
        if copyright_re.match(line) and lineno < len(msgstr_lines) and line != msgstr_lines[lineno]:
            return (0,error_string)
        lineno+=1
    return (1,'')

if __name__ == '__main__':
    import sys
    msgid = sys.stdin.readline()
    msgstr = sys.stdin.readline()
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print 'Success'

# Local Variables:
# coding: utf-8
# End:
