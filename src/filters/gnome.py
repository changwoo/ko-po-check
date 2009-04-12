# GNOME specific rule

name = "gnome"

import string,localeutil
e = localeutil.eucstr

error_string = e("GNOME���� \"translator_credits\"���� �����ڵ��� �̸��� ��� �մϴ�")

def check(msgid,msgstr):
    if (msgid[:18] == "translator_credits" and
        (msgstr[:18] == "translator_credits" or msgstr[:6] == e("����"))):
        return (0,error_string)
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
