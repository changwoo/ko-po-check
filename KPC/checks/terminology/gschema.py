# -*- coding: utf-8 -*-

# 그놈 프로그램 gschema에서 많이 쓰이는 메시지 통일

from KPC.classes import Error, BaseCheck

data = [
    {'msgid': 'Window maximized',
     'msgstr': '창 최대화'},
    {'msgid': 'Window maximized state.',
     'msgstr': '창 최대화 상태.'},
    {'msgid': 'Window size',
     'msgstr': '창 크기'},
    {'msgid': 'Window size (width and height).',
     'msgstr': '창 크기(너비 및 높이).'},
    {'msgid': 'Window position.',
     'msgstr': '창 위치'},
    {'msgid': 'Window position (x and y).',
     'msgstr': '창 위치(가로 및 세로).'},
]


class GschemaCheck(BaseCheck):
    errstr = '일관성을 위해 다음과 같이 번역합니다: %s'

    def check(self, entry, context):
        if not True in [('.gschema' in p) for p in entry.references]:
            return []
        for d in data:
            if entry.msgid.lower() != d['msgid'].lower():
                continue
            if entry.msgstr != d['msgstr']:
                return [Error(self.errstr % d['msgstr'])]
        return []

name = 'terminology/gschema'
description = 'gschema에서 자주 사용하는 메시지의 번역이 통일된 번역인지 검사합니다'
checker = GschemaCheck()
