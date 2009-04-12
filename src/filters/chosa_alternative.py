#!/usr/bin/python

import re,string

name = "should-have-chosa-alternative"

import localeutil
e = localeutil.eucstr

chosa_data = [(e('��'),e('��'),e('��(��)')),
              (e('��'),e('��'),e('��(��)')),
              (e('��'),e('��'),e('��(��)')),
              (e('��'),e('����'),e('(��)��')),
              (e('�μ�'),e('���μ�'),e('(��)�μ�')),
              (e('�ν�'),e('���ν�'),e('(��)�ν�')),
              (e('�κ���'),e('���κ���'),e('(��)�κ���')),
              (e('���'),e('�̶��'),e('(��)���'))]

def chosa_suggest(cho):
    for (a,b,s) in chosa_data:
        if cho == a or cho == b:
            return s
    return '????'

format = "%([1-9][0-9]*\$)?[-+ #'0]*([1-9][0-9]*)?(\.[0-9]+)?((hh|h|j|l|L|ll|q|t|z|Z)?[dioufeEgGaAcCspnmhjlLqtxXzZ1-9]|hh|ll)"
chosa = "(" + string.join(map(lambda p: p[0]+"|"+p[1], chosa_data),'|') + ")"

chosa_re = re.compile("(("+format+"['\"]?) ?"+chosa+")(\s|$)")
error_string = e("\"%s\": ��ħ�� ���� ���� ������ �����ϴ�. '%s'")

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    while 1:
        mo = chosa_re.search(msgstr)
        if mo and (mo.end() >= len(msgstr) or msgstr[mo.end()] != '('):
            ret = 0
            if errmsg:
                errmsg += '\n'
            sug = mo.group(2) + chosa_suggest(mo.group(8))
            errmsg += error_string % (mo.group(1),sug)
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
