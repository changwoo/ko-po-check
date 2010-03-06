# -*- coding: utf-8 -*-

import string, re
from KPC.classes import Error, BaseCheck

class CopyrightCheck(BaseCheck):
    copyright_re = re.compile(r"^([Cc]opyright )?\([Cc]\) ")
    error = Error('copyright notice는 번역하면 안 됩니다')
    def check(self, entry):
        msgid_lines = string.split(entry.msgid,"\n")
        msgstr_lines = string.split(entry.msgstr,"\n")
        for (msgid, msgstr) in zip(msgid_lines, msgstr_lines):
            if self.copyright_re.match(msgid) and msgid != msgstr:
                return [self.error]
        return []

name = 'convention/copyright'
description = '저작권 표시에 대한 번역문을 검사합니다'
checker = CopyrightCheck()
