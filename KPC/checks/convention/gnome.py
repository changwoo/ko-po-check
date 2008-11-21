# -*- coding: utf-8 -*-
# GNOME specific rule

name = 'convention/gnome'
description = "그놈 프로젝트에서 사용하는 관행에 맞는지 검사합니다"

error_string = u'GNOME에서 \"translator_credits\"에는 번역자들의 이름을 써야 합니다'

def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
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
