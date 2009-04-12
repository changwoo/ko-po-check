#!/usr/bin/python

import re

name = "common-misspell"

def euc(s):
    return unicode(s,'euc-kr').encode('utf-8')

misspell_data = [
    { 're':    re.compile(euc("(��\s*��)")),
      'error': euc("\"%s\": '��'�� �ƴ϶� '��'�Դϴ�") },
    { 're':    re.compile(euc("(���ϴ�)")),
      'error': euc("\"%s\": '���ϴ�'�� �ƴ϶� '���ϴ�'�Դϴ�") },
    { 're':    re.compile("((��|��)��)"),
      'error': euc("\"%s\": '��'�� �ƴ϶� '��'�Դϴ�") }
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
