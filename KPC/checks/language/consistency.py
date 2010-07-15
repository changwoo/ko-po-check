# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

data = [
    { 're': re.compile(u'.*[^\.]\.$'),
      'except': re.compile(u'.*(\)|etc|No|a\.m|p\.m)\.$'),
      'error':  Error('번역문이 원문과 같이 .으로 끝나야 합니다') },
    { 're': re.compile(u'.*:$'),
      'error':  Error('번역문이 원문과 같이 :으로 끝나야 합니다') },
    { 're': re.compile(u'.*[^\s]\.\.\.$'),
      'except': re.compile(u'.*(etc)\.\.\.$'),
      'error':  Error('번역문이 원문과 같이 ...으로 끝나야 합니다') },
    { 're': re.compile(u'.*…$'),
      'error':  Error('번역문이 원문과 같이 …으로 끝나야 합니다') },
    ]
    
class ConsistencyCheck(BaseCheck):
    def check(self, entry):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        for d in data:
            re = d['re']
            error = d['error']
            if (re.match(msgid) and
                (not d.has_key('except') or not d['except'].match(msgid)) and
                not re.match(msgstr)):
                errors.append(error)
        return errors

name = 'language/consistency'
description = '번역문이 원문과 비슷한 문장 부호로 끝나도록 합니다'
checker = ConsistencyCheck()
