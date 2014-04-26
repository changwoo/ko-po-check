# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

data = [
    {
        're': re.compile('.*[^\.]\.$'),
        'except': re.compile('.*(\)|etc|No|a\.m|p\.m)\.$'),
        'error':  Error('번역문이 원문과 같이 .으로 끝나야 합니다')
    },
    {
        're': re.compile('.*:$'),
        'error':  Error('번역문이 원문과 같이 :으로 끝나야 합니다')
    },
    {
        're': re.compile('.*[^\s]\.\.\.$'),
        'except': re.compile('.*(etc)\.\.\.$'),
        'error':  Error('번역문이 원문과 같이 ...으로 끝나야 합니다')
    },
    {
        're': re.compile('.*…$'),
        'error':  Error('번역문이 원문과 같이 …으로 끝나야 합니다')
    },
]


class ConsistencyCheck(BaseCheck):
    def check(self, entry, context):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        for d in data:
            re = d['re']
            error = d['error']
            if not re.match(msgid):
                continue
            if 'except' in d and d['except'].match(msgid):
                continue
            if not re.match(msgstr):
                errors.append(error)
        return errors

name = 'language/consistency'
description = '번역문이 원문과 비슷한 문장 부호로 끝나도록 합니다'
checker = ConsistencyCheck()
