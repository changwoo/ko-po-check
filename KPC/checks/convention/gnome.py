# -*- coding: utf-8 -*-
# GNOME specific rule

from KPC.classes import Error, BaseCheck


class GnomeCheck(BaseCheck):
    error = Error('그놈 번역 규칙에 따라 번역자의 이름을 써야 합니다')

    def check(self, entry, context):
        msgid = entry.msgid
        msgstr = entry.msgstr
        if not msgid[:18] in ('translator-credits', 'translator_credits'):
            return []
        if msgstr[:18] in ('translator-credits', 'translator_credits'):
            return [self.error]
        if msgstr[:2] == '번역':
            return [self.error]
        return []

name = 'convention/gnome'
description = '그놈 프로젝트에서 사용하는 관행에 맞는지 검사합니다'
checker = GnomeCheck()
