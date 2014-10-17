# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

# 괄호 띄어쓰기
check_list = [
    { 're': re.compile('[\uac00-\ud7a3] \((?!%a)', re.UNICODE),
      'msg': '맞춤법 규정에 따라 괄호 앞에 띄어 쓰지 않습니다',
    },
    { 'check': lambda e: True not in [('.desktop' in p) for p in e.references],
      're': re.compile('\s([A-Za-z\uac00-\ud7a3]*[\uac00-\ud7a3];)\s+', re.UNICODE | re.MULTILINE),
      'msg': '우리말 맞춤법에서는 세미콜론을 쓰지 않습니다',
    },
]

class PunctuationCheck(BaseCheck):
    def check(self, entry, context):
        msgstr = entry.msgstr
        errors = []
        for i in check_list:
            if 'check' in i and not i['check'](entry):
                continue
            mo = i['re'].search(msgstr)
            if mo:
                errors.append(Error(i['msg']))
        return errors

name = 'language/punctuation'
description = '잘못된 한국어 구문 규칙을 찾아냅니다'
checker = PunctuationCheck()
