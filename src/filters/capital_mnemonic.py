#!/usr/bin/python

import re

name = "mnemonic-must-be-capital"

import localeutil
e = localeutil.eucstr

search_re = re.compile("(\([_&][a-z]\))")
error_string = e("\"%s\": mnemonic이 소문자입니다")

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    while 1:
        mo = search_re.search(msgstr)
        if mo:
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += error_string % msgstr[mo.start():mo.end()]
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
