#!/usr/bin/python

import re

name = "common-misspell"

misspell_data = [
    { 're':    re.compile("(��\s*��)"),
      'error': "\"%s\": '��'�� �ƴ϶� '��'�Դϴ�" },
    { 're':    re.compile("(���ϴ�)"),
      'error': "\"%s\": '���ϴ�'�� �ƴ϶� '���ϴ�'�Դϴ�" }
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
