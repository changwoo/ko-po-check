#!/usr/bin/python

import re

name = "should-have-chosa-alternative"

chosa_re = re.compile("(%[cdfs](��|��|��|��|�μ�|�ν�|��|���μ�|���ν�|����|�ν�))")
error_string = "\"%s\": ���翡 ���� ��ħ ������ �����ϴ�" 
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
