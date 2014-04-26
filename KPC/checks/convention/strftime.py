# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

R = re.compile

data = [
    # 월 일
    (R('(%[-_0-9^]?[bB]) (%[-_0-9^]?[de])'), '{0} {1}일'),
    # 일 월
    (R('(%[-_0-9^]?[de]) (%[-_0-9^]?[bB])'), '{1} {0}일'),

    # 요일 일 월 년
    (R('(%[-_0-9^]?A) (%[-_0-9^]?[de]) (%[-_0-9^]?[bB]) (%[-_0-9^]?Y)'),
     '{3}년 {2} {1}일 {0}'),
    # 요일 일 월
    (R('(%[-_0-9^]?A) (%[-_0-9^]?[de]) (%[-_0-9^]?[bB])'), '{2} {1}일 {0}'),
    # 요일 일 월
    (R('(%[-_0-9^]?a) (%[-_0-9^]?[de]) (%[-_0-9^]?[bB])'),
     '{2} {1}일 ({0})'),

    # 요일 월 일 년
    (R('(%[-_0-9^]?A) (%[-_0-9^]?[bB]) (%[-_0-9^]?[de]) (%[-_0-9^]?Y)'),
     '{3}년 {1} {2}일 {0}'),
    # 요일 월 일
    (R('(%[-_0-9^]?A) (%[-_0-9^]?[bB]) (%[-_0-9^]?[de])'), '{1} {2}일 {0}'),
    # 요일 월 일
    (R('(%[-_0-9^]?a) (%[-_0-9^]?b) (%[-_0-9^]?[de])'), '{1} {2}일 ({0})'),

    # 요일 24시각
    (R('(%[-_0-9^]?a) (%[-_0-9^]?R)'), '({0}) {1}'),

    # 요일 시각 오전/오후
    (R('(%[-_0-9^]?a) ' +
       '(%[-_0-9^]?[lI](?:[:\u2236]%[-_0-9^]?M(?:[:\u2236]%[-_0-9^]?S)?)?) ' +
       '(%[pP])'),
     '({0}) {2} {1}'),

    # 시각 오전/오후
    (R('(%[-_0-9^]?[lI](?:[:\u2236]%[-_0-9^]?M(?:[:\u2236]%[-_0-9^]?S)?)?) ' +
       '(%[pP])'),
     '{1} {0}'),

    # 월 년
    (R('(%[-_0-9^]?[bB]) (%[-_0-9^]?Y)'), '{1}년 {0}'),

    # 월 일 년
    (R('(%[-_0-9^]?[bB]) (%[-_0-9^]?[de]) (%[-_0-9^]?Y)'),
     '{2}년 {0} {1}일'),
    # 일 월 년
    (R('(%[-_0-9^]?[de]) (%[-_0-9^]?[bB]) (%[-_0-9^]?Y)'),
     '{2}년 {1} {0}일'),

    # 요일 월/일/년
    (R('(%[-_0-9^]?a) (%[-_0-9^]?m)/(%[-_0-9^]?[de])/(%[-_0-9^]?Y)'),
     '{3}/{1}/{2} ({0})'),

    # 월/일/년
    (R('(%[-_0-9^]?m)/(%[-_0-9^]?[de])/(%[-_0-9^]?Y)'), '{2}/{0}/{1}'),

    # 일-월-년 (%b => %m)
    (R('(%[-_0-9^]?[de])-%([-_0-9^])?b-(%[-_0-9^]?Y)'), '{2}-%{1}m-{0}'),
]


class StrftimeCheck(BaseCheck):
    errstr = '%s: 날짜/시간, 다음과 같이 번역합니다: %s'

    def identify(self, entry):
        if entry.is_c_format():
            return False
        return True

    def check(self, entry, context):
        if not self.identify(entry):
            return []
        errors = []
        for (origre, transfmt) in data:
            m = origre.search(entry.msgid)
            if not m:
                continue
            orig = m.group(0)
            matched = [m.group(i + 1) or '' for i in range(0, origre.groups)]
            trans = transfmt.format(*matched)

            if not trans in entry.msgstr:
                errors.append(Error(self.errstr % (orig, trans)))
        return errors


name = 'convention/strftime'
description = 'strftime() 포맷을 확인합니다'
checker = StrftimeCheck()
