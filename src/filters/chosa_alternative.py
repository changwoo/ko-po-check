#!/usr/bin/python

import re

name = "should-have-chosa-alternative"

chosa_re = re.compile("(%([1-9]\$)?[cdfs][\"\']?(이|가|을|를|은|는|로서|로써|로|으로서|으로써|으로|로써))")
error_string = "\"%s\": 받침에 따른 조사 구별(예: %%s을(를))이 없습니다" 
def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    while 1:
        mo = chosa_re.search(msgstr)
        if mo and (mo.end() >= len(msgstr) or msgstr[mo.end()] != '('):
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
