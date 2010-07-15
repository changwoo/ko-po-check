# -*- coding: utf-8 -*-

import re, string
from KPC.classes import Error, BaseCheck

data = [('%a %b %e', '%b %e일 (%a)'),
        ('%a %b %d', '%b %d일 (%a)'),
        ('%b %e', '%b %e일'),
        ('%B %e', '%B %e일'),
        ('%b %d', '%b %d일'),
        ('%B %d', '%B %d일'),
        ('%A %d %b %Y', '%Y년 %b %d일 %A'),
        ('%A %d %b', '%b %d일 %A'),
        ('%A %d %B %Y', '%Y년 %B %d일 %A'),
        ('%A %d %B', '%B %d일 %A'),
        ('%l:%M:%S %p', '%p %l:%M:%S'),
        ('%l:%M %p', '%p %l:%M'),
        ('%I:%M:%S %p', '%p %I:%M:%S'),
        ('%I:%M %p', '%p %I:%M'),
        ('%I %p', '%p %I'),
        ('%A, %B %d, %Y', '%Y년 %B %d일 %A'),
        ('%A, %B %e, %Y', '%Y년 %B %e일 %A'),
        ('%A, %B %d', '%B %d일 %A'),
        ('%A, %B %e', '%B %e일 %A'),
        ('%B %Y', '%Y년 %B'),
        ('%d %B %Y', '%Y년 %B %d일'),
        ('%e %B %Y', '%Y년 %B %e일'),
        ('%a %m/%d/%Y', '%Y/%m/%d (%a)'),
        ('%m/%d/%Y', '%Y/%m/%d'),
        ('%d-%b-%Y', '%Y-%m-%d'),
    ]

class StrftimeCheck(BaseCheck):
    errstr = '%s: 날짜/시간, 다음과 같이 번역합니다: %s'
    def identify(self, entry):
        if entry.is_c_format():
            return False
        return True

    def check(self, entry):
        if not self.identify(entry):
            return []
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        for (orig, trans) in data:
            if orig in entry.msgid and not trans in entry.msgstr:
                errors.append(Error(self.errstr % (orig, trans)))
        return errors
        
name = 'convention/strftime'
description = 'strftime() 포맷을 확인합니다'
checker = StrftimeCheck()
