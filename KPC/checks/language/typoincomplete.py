# -*- coding: utf-8 -*-

import sys
import string,re
from KPC.classes import Error, BaseCheck

typo_re = re.compile('([\u3131-\u318E]+)')
typo_exception_re = re.compile('^[\u3131-\u318E]-[\u3131-\u318E]') # gdm
typo_error = '\"%s\": 음절이 불완전합니다.  오타로 보입니다'

class TypoIncompleteCheck(BaseCheck):
    def check(self, entry):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        s = msgstr
        while 1:
            mo = typo_re.search(s)
            if mo and not typo_exception_re.match(s):
                errors.append(Error(typo_error % mo.group(1)))
                s = s[mo.end():]
            else:
                break;
        return errors

name = 'language/typoincomplete'
description = '오타로 보이는 불완전한 음절을 찾아냅니다'
checker = TypoIncompleteCheck()
