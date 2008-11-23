# -*- coding: utf-8 -*-
# markup translation
# Ref: http://developer.gnome.org/doc/API/2.0/pango/PangoMarkupFormat.html

name = 'convention/markup-pango'
description = "판고 마크업의 짝이 맞는지 검사합니다"

import re, string

tags = [ 'span', 'b', 'big', 'i', 's', 'sub', 'sup', 'small', 'tt', 'u' ]
tags_res = '(' + string.join(tags, '|') + ')'
re_markup = re.compile('<(' + tags_res + '[^>]*)>[^<]+</' + tags_res + '>')
group_opentag = 1
group_opentagname = 2
group_closetag = 3
group_closetagname = 3

error_string = u'<%s>: 번역할 때 마크업을 똑같이 써야 합니다'

def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    mo = re_markup.search(msgid)
    while mo:
        tagname = mo.group(group_opentagname)
        opentag = mo.group(group_opentag)
        mo = re.search('<' + opentag + '>.+</' + tagname + '>', msgstr, re.M)
        if not mo:
            return (0, error_string % opentag)
        msgid = msgid[mo.start(0) + 1:]
        mo = re_markup.search(msgid)
    return (1,'')

if __name__ == '__main__':
    import sys
    class entry:
        pass
    entry.msgid = sys.stdin.readline()
    entry.msgstr = sys.stdin.readline()
    t,e = check(entry)
    if not t:
        print e
    else:
        print 'Success'
