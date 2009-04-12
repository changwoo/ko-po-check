#!/usr/bin/python

import re

name = "should-have-chosa-alternative"

def euc(s):
    return unicode(s,'euc-kr').encode('utf-8')

format = "%([1-9][0-9]*\$)?[-+ #'0]*([1-9][0-9]*)?(\.[0-9]+)?((hh|h|j|l|L|ll|q|t|z|Z)?[dioufeEgGaAcCspnmhjlLqtxXzZ1-9]|hh|ll)"
chosa = "(��|��|��|��|��|��|��|����|�μ�|���μ�|�ν�|���ν�|�κ���|���κ���|���|�̶��)"

chosa_re = re.compile(euc("("+format+"['\"]? ?"+chosa+")(\s|$)"))
error_string = euc("\"%s\": ��ħ�� ���� ���� ����(��: %%s��(��))�� �����ϴ�")
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
