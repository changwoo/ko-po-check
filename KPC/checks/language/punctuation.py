# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

# 괄호 띄어쓰기
check_list = [
    [
        re.compile('[\uac00-\ud7a3] \(\S', re.UNICODE),
        '맞춤법 규정에 따라 괄호 앞에 띄어 쓰지 않습니다'
    ]
]


class PunctuationCheck(BaseCheck):
    def check(self, entry, context):
        msgstr = entry.msgstr
        errors = []
        for (r, emsg) in check_list:
            mo = r.search(msgstr)
            if mo:
                errors.append(Error(emsg))
        return errors

name = 'language/punctuation'
description = '잘못된 한국어 구문 규칙을 찾아냅니다'
checker = PunctuationCheck()
