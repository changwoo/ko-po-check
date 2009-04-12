import string

name = "gnome-glossary"

import localeutil
e = localeutil.eucstr

data = [("properties", e("��� ����"), e("�Ӽ�")),
        ("preferences", e("�⺻ ����"), e("���� ����")),
        ("preferences", e("�⺻ ����"), e("ȯ�漳��")),
        ("about", e("����"), e("���Ͽ�")),
        ("font", e("�۲�"), e("��Ʈ")),
        ]

error_string = e("%s: �׳� ����ũž���� \"%s\"��(��) \"%s\"(��)��� ����")

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    for (id, right, wrong) in data:
        if ((string.find(msgstr, wrong) >= 0) and
            (string.find(string.lower(msgid), id) >= 0) and
            (string.find(msgstr, right) < 0)):
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += error_string % (wrong, id, right)
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
