#!/usr/bin/python

import re

name = "common-misspell"

def euc(s):
    return unicode(s,'euc-kr').encode('utf-8')

misspell_data = [
    { 're':    re.compile(euc("(않\s*(한|함|합니다|된|됨|됩니다))")),
      'error': euc("\"%s\": 짧은 부정문에서는 '않'이 아니라 '안'을 씁니다") },
    { 're':    re.compile(euc("(읍니다)")),
      'error': euc("\"%s\": '읍니다'가 아니라 '습니다'입니다") },
    { 're':    re.compile("((없|있|남았)슴)"),
      'error': euc("\"%s\": '슴'이 아니라 '음'입니다") }
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
