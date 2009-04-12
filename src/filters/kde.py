# GNOME specific rule

name = "kde"

import string,localeutil
e = localeutil.eucstr

error0_string = e("KDE���� \"_:\"���� ù ��° \\n������ ���𸻿� ���� �����̹Ƿ� �����ϸ� �� �˴ϴ�.")
error1_string = e("������ �̸��� ��� �մϴ�.  \"_:\"�� �����ϴ� ������ �����ϸ� �� �˴ϴ�.")
error2_string = e("������ �̸����� ��� �մϴ�  \"_:\"�� �����ϴ� ������ �����ϸ� �� �˴ϴ�.")

def check(msgid,msgstr):
    if (msgstr[:3] == "_: "):
        return (0,error0_string)
    if (msgid[:22] == "_: NAME OF TRANSLATORS" and
        (msgstr[:3] == "_: " or string.find(msgstr,e("����")) >= 0)):
        return (0,error1_string)
    if (msgid[:23] == "_: EMAIL OF TRANSLATORS" and
        (msgstr[:3] == "_: " or string.find(msgstr,e("����")) >= 0)):
        return (0,error2_string)
    return (1,"")

if __name__ == '__main__':
    import sys
    msgid = sys.stdin.readline()
    msgstr = sys.stdin.readline()
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print "Success"
