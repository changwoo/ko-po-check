# -*- coding: utf-8 -*-
# GNOME specific rule

name = "gnome"

e = lambda s: unicode(s,'utf-8')

error_string = e("GNOME에서 \"translator_credits\"에는 번역자들의 이름을 써야 합니다")

def check(msgid,msgstr):
    if (msgid[:18] == "translator_credits" and
        (msgstr[:18] == "translator_credits" or msgstr[:2] == e("번역"))):
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

# Local Variables:
# coding: utf-8
# End:
