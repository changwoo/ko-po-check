# GNOME specific rule

name = "kde"

import string,localeutil
e = localeutil.eucstr

error1_string = e("KDE에서 번역자들의 이름을 써야 합니다.  \"_:\"은 안 써도 됩니다")
error2_string = e("KDE에서 번역자들의 이메일을 써야 합니다  \"_:\"은 안 써도 됩니다")

def check(msgid,msgstr):
    if (msgid[:22] == "_: NAME OF TRANSLATORS" and
        (msgstr[:3] == "_: " or string.find(msgstr,e("번역")) >= 0)):
        return (0,error1_string)
    if (msgid[:23] == "_: EMAIL OF TRANSLATORS" and
        (msgstr[:3] == "_: " or string.find(msgstr,e("번역")) >= 0)):
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
