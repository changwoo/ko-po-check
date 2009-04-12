#!/usr/bin/python

import string,re

name = "common-misspell"

e = lambda s: unicode(s,'euc-kr')

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
    "��",
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

# ���� ����
chosa_re = "("+string.join([
    '��','��','��\(��\)',
    '��','��','��\(��\)',
    '��','��','��\(��\)',
    '��','����','\(��\)��',
    '�μ�','���μ�','\(��\)�μ�',
    '�ν�','���ν�','\(��\)�ν�',
    '�κ���','���κ���','\(��\)�κ���',
    '���','�̶��','\(��\)���',
    '��', '��', '��', '����', '��', '����',
    ], '|')+")"

def test_noun_suffix(str):
    if (str[-1] != e('��')):
        return 1
    elif ((ord(str[-2]) - 0xac00) % 28 == 20):
        return 0
    elif (str[-2] == e('��')):
        return 0
    else:
        return 1
    

misspell_data = [
    { 're':    re.compile(e("(��\s*(��|��|�մϴ�|��|��|�˴ϴ�))")),
      'error': e("\"%s\": ª�� ������������ '��'�� �ƴ϶� '��'�� ���ϴ�") },
    { 're':    re.compile(e("(���ϴ�)")),
      'error': e("\"%s\": '���ϴ�'�� �ƴ϶� '���ϴ�'�Դϴ�") },
    { 're':    re.compile(e("([^\s]+��)([\s\.\,\?]|$)")),
      'func':  test_noun_suffix,
      'error': e("\"%s\": '��'�� �ƴ϶� '��'�Դϴ�") },
    { 're':    re.compile(e("("+verbs_re+"��(��|��|��)?\s"+")")),
      'error': e("\"%s\": ���� ���� ��� ��� �մϴ�") },
    { 're':    re.compile(e("("+verbs_re+"\s*��(��|��)"+")")),
      'error': e("\"%s\": ���� ���� ��� ��� �մϴ�") },
    { 're':    re.compile(e("("+verbs_re+"��(��|��|��)?\s"+")")),
      'error': e("\"%s\": `~�� ��'��� ��� ��� �մϴ�") },
    { 're':    re.compile(e("([0-9A-Za-z-+`'\"()%_]+\s+"+chosa_re+")\s+")),
      'error': e("\"%s\": ����� ü�� �ٿ� ��� �մϴ�") },
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
                if (data.has_key('func') and data['func'](mo.group(1))):
                    str = str[mo.end():]
                    continue
                ret = 0
                if errmsg:
                    errmsg += '\n'
                errmsg += misspell_error % mo.group(1)
                str = str[mo.end():]
            else:
                break;
    return (ret, errmsg)    

if __name__ == '__main__':
    import sys
    msgid = unicode(sys.stdin.readline(),'euckr')
    msgstr = unicode(sys.stdin.readline(),'euckr')
    t,e = check(msgid,msgstr)
    if not t:
        print e.encode('euckr')
    else:
        print "Success"
