#!/usr/bin/python

import re

chosa_re = re.compile("(%[cdfs](��|��|��|��|��|����|�μ�|���μ�|�ν�|���ν�))[^A-Za-z0-9\xb0-\xfe]")
error_string = "\"%s\": ���翡 ���� ��ħ ������ �����ϴ�" 
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
