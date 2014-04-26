# -*- coding: utf-8 -*-
# markup translation
# Ref: http://developer.gnome.org/doc/API/2.0/pango/PangoMarkupFormat.html

import re
from KPC.classes import Error, BaseCheck

tags = ['span', 'b', 'big', 'i', 's', 'sub', 'sup', 'small', 'tt', 'u']
tags_res = '(' + '|'.join(tags) + ')'
re_markup = re.compile('<(' + tags_res + '( [^>]*)?)>')
group_opentag = 1
group_opentagname = 2

error_string = '<%s>: 번역할 때 마크업을 똑같이 써야 합니다'


class MarkupPangoCheck(BaseCheck):
    def check(self, entry, context):
        msgid = entry.msgid
        msgstr = entry.msgstr
        mo = re_markup.search(msgid)
        while mo:
            tagname = mo.group(group_opentagname)
            opentag = mo.group(group_opentag)
            mo = re.search('<' + opentag + '>.+</' + tagname + '>', msgstr,
                           re.M | re.S)
            if not mo:
                return [Error(error_string % opentag)]
            msgid = msgid[mo.start(0) + 1:]
            mo = re_markup.search(msgid)
        return []

name = 'convention/markup-pango'
description = '판고 마크업의 짝이 맞는지 검사합니다'
checker = MarkupPangoCheck()
