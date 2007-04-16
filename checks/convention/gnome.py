# -*- coding: utf-8 -*-
# GNOME specific rule

name = 'convention/gnome'

error_string = u'GNOME에서 \"translator_credits\"에는 번역자들의 이름을 써야 합니다'

def check(msgid,msgstr):
    if ((msgid[:18] == 'translator_credits' or
         msgid[:18] == 'translator-credits') and
        (msgstr[:18] == 'translator_credits' or msgstr[:2] == u'번역')):
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
        print 'Success'

# Local Variables:
# coding: utf-8
# End:
