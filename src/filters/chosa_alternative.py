#!/usr/bin/python

import re

name = "should-have-chosa-alternative"

import localeutil
e = localeutil.eucstr

format = "%([1-9][0-9]*\$)?[-+ #'0]*([1-9][0-9]*)?(\.[0-9]+)?((hh|h|j|l|L|ll|q|t|z|Z)?[dioufeEgGaAcCspnmhjlLqtxXzZ1-9]|hh|ll)"
chosa = "(��|��|��|��|��|��|��|����|�μ�|���μ�|�ν�|���ν�|�κ���|���κ���|���|�̶��)"

chosa_re = re.compile(e("("+format+"['\"]? ?"+chosa+")(\s|$)"))
error_string = e("\"%s\": ��ħ�� ���� ���� ����(��: %%s��(��))�� �����ϴ�")
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
