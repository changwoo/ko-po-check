# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck


class CopyrightCheck(BaseCheck):
    copyright_re = re.compile('^([Cc]opyright )?\([Cc]\) ')
    error = Error('copyright notice는 번역하면 안 됩니다')

    def check(self, entry, context):
        msgid_lines = entry.msgid.split('\n')
        msgstr_lines = entry.msgstr.split('\n')
        for (msgid, msgstr) in zip(msgid_lines, msgstr_lines):
            if self.copyright_re.match(msgid) and msgid != msgstr:
                return [self.error]
        return []

name = 'convention/copyright'
description = '저작권 표시에 대한 번역문을 검사합니다'
checker = CopyrightCheck()
