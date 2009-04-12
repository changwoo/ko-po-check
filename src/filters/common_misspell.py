#!/usr/bin/python

import string,re

name = "common-misspell"

import localeutil
e = localeutil.eucstr

# ������縦 ���� -�� ������ ���� ����
verbs_re = "("+string.join([
    "������",
    "��",
    "��",
    "��ĥ"
    "��Ÿ��",
    "����",
    "����",
    "�ǵ���",
    "����",
    "�ٲ�",
    "����",
    "��",
    "����",
    "��ų",
    "��",
    "��"
    "��",
    "����",
    "����",
    "��",
    "��",
    "��",
    "�о����",
    "����",
    "����",
    "���",
    "����",
    "ã��",
    "��",
    ], '|')+")"

variations_re = "(�ִ�|����|�ֽ��ϴ�|�����ϴ�|�ִ�|����|�ְ�|����)"

misspell_data = [
    { 're':    re.compile(e("(��\s*(��|��|�մϴ�|��|��|�˴ϴ�))")),
      'error': e("\"%s\": ª�� ������������ '��'�� �ƴ϶� '��'�� ���ϴ�") },
    { 're':    re.compile(e("(���ϴ�)")),
      'error': e("\"%s\": '���ϴ�'�� �ƴ϶� '���ϴ�'�Դϴ�") },
    { 're':    re.compile(e("((��|��|����)��)")),
      'error': e("\"%s\": '��'�� �ƴ϶� '��'�Դϴ�") },
    { 're':    re.compile(e("("+verbs_re+"��(��|��|��)?\s"+")")),
      'error': e("\"%s\": ���� ���� ��� ��� �մϴ�") },
    { 're':    re.compile(e("("+verbs_re+"\s*��(��|��)"+")")),
      'error': e("\"%s\": ���� ���� ��� ��� �մϴ�") },
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
