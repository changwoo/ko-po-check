# -*- coding: utf-8 -*-
# extra space

from KPC.classes import Error, BaseCheck


class ExtraSpaceCheck(BaseCheck):
    def check(self, entry, context):
        msgid = entry.msgid
        msgstr = entry.msgstr

        if msgstr[-1].isspace() and msgid != '' and msgstr[-1] != msgid[-1]:
            return [Error('끝에 불필요하게 공백 문자가 있습니다')]
        return []

name = 'convention/extra-space'
description = '불필요한 공백 문자 검사'
checker = ExtraSpaceCheck()
