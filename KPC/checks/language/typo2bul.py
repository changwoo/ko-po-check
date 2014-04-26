# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

typo = '('+'|'.join([
    '밍나합니다',
    '거싱',
    '살마',
    '[가-힣]빈다'
    ])+')'

typo_re = re.compile(typo)
typo_error = '\"%s\": 두벌식 오타로 보입니다'


class Typo2BulCheck(BaseCheck):
    def check(self, entry, context):
        msgstr = entry.msgstr
        errors = []
        s = msgstr
        while 1:
            mo = typo_re.search(s)
            if mo:
                errors.append(Error(typo_error % mo.group(1)))
                s = s[mo.end():]
            else:
                break
        return errors

name = 'language/typo2bul'
description = '두벌식 키보드를 사용할 때 발생할 수 있는 오타를 찾아냅니다'
checker = Typo2BulCheck()
