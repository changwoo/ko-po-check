import string

name = "gnome-glossary"

data = [("properties", "��� ����", "�Ӽ�"),
        ("preferences", "�⺻ ����", "���� ����"),
        ("preferences", "�⺻ ����", "ȯ�漳��"),
        ("about", "����", "���Ͽ�"),
        ("font", "�۲�", "��Ʈ"),
        ]
error_string = "%s: �׳� ����ũž���� \"%s\"��(��) \"%s\"(��)��� ����"

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
