#!/usr/bin/python

import re

name = "common-misspell"

misspell_data = [
    { 're':    re.compile("(않\s*함)"),
      'error': "\"%s\": '않'이 아니라 '안'입니다" },
    { 're':    re.compile("(읍니다)"),
      'error': "\"%s\": '읍니다'가 아니라 '습니다'입니다" }
]

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    for data in misspell_data:
        misspell_re = data['re']
        misspell_error = data['error']
        str = msgstr
        while 1:
            mo = misspell_re.search(str)
            if mo:
                ret = 0
                if errmsg:
                    errmsg += '\n'
                errmsg += misspell_error % str[mo.start(1):mo.end(1)]
                str = str[mo.end():]
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
