# -*- coding: utf-8 -*-
# markup translation
# Ref: http://developer.gnome.org/doc/API/2.0/pango/PangoMarkupFormat.html

name = "markup"

e = lambda s: unicode(s,'utf-8')

import re, string

tags = [ "span", "b", "big", "i", "s", "sub", "sup", "small", "tt", "u" ]
tags_res = "(" + string.join(tags, "|") + ")"
re_markup = re.compile("<(" + tags_res + "[^>]*)>.*</" + tags_res + ">")
group_opentag = 1
group_opentagname = 2
group_closetag = 3
group_closetagname = 3

error_string = e("<%s>: 번역할 때 마크업을 똑같이 써야 합니다")

def check(msgid,msgstr):
    mo = re_markup.match(msgid)
    if mo and mo.group(group_opentagname) == mo.group(group_closetagname):
        tagname = mo.group(group_opentagname)
        opentag = mo.group(group_opentag)
        mo = re_markup.match(msgstr)
        if not mo or mo.group(group_opentagname) != tagname or mo.group(group_closetagname) != tagname or mo.group(group_opentag) != opentag:
            return (0, error_string % opentag)
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
