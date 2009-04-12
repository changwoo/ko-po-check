import string

name = "gnome-glossary"

def euc(s):
    return unicode(s,'euc-kr').encode('utf-8')

data = [("properties", euc("��� ����"), euc("�Ӽ�")),
        ("preferences", euc("�⺻ ����"), euc("���� ����")),
        ("preferences", euc("�⺻ ����"), euc("ȯ�漳��")),
        ("about", euc("����"), euc("���Ͽ�")),
        ("font", euc("�۲�"), euc("��Ʈ")),
        ]

error_string = euc("%s: �׳� ����ũž���� \"%s\"��(��) \"%s\"(��)��� ����")

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
