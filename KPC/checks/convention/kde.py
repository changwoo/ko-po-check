# -*- coding: utf-8 -*-
# GNOME specific rule

name = 'convention/kde'

error0_string = u'KDE에서 \"_:\"부터 첫 번째 \\n까지는 본디말에 대한 설명이므로 번역하면 안 됩니다.'
error1_string = u'번역자 이름을 써야 합니다. \"_:\"로 시작하는 문장은 번역하면 안 됩니다.'
error2_string = u'번역자 이메일을 써야 합니다. \"_:\"로 시작하는 문장은 번역하면 안 됩니다.'

def check(msgid,msgstr):
    import string
    if (msgstr[:3] == '_: '):
        return (0,error0_string)
    if (msgid[:22] == '_: NAME OF TRANSLATORS' and
        (msgstr[:3] == '_: ' or string.find(msgstr,u'번역') >= 0 or
         string.find(msgstr,u'옮긴이') >= 0)):
        return (0,error1_string)
    if (msgid[:23] == '_: EMAIL OF TRANSLATORS' and
        (msgstr[:3] == '_: ' or string.find(msgstr,u'번역') >= 0 or
         string.find(msgstr,u'옮긴이') >= 0)):
        return (0,error2_string)
    return (1,'')

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
