#!/usr/bin/python

import re

chosa_re = re.compile("(%[cdfs](이|가|을|를|로|으로|로서|으로서|로써|으로써))[^A-Za-z0-9\xb0-\xfe]")
error_string = "\"%s\": 조사에 따른 받침 구별이 없습니다" 
def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    while 1:
        mo = chosa_re.search(msgstr)
        if mo:
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += error_string % msgstr[mo.start(1):mo.end(1)]
            msgstr = msgstr[mo.end():]
        else:
            break;
    return (ret, errmsg)    

if __name__ == '__main__':
    import sys
    msgid = sys.stdin.readline()
    msgstr = sys.stdin.readline()
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print "Success"
