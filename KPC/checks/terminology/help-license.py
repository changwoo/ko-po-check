# -*- coding: utf-8 -*-

# 그놈 프로그램의 도움말 문서의 법률 정보 페이지에 공통으로 많이
# 사용하는 Creative Commons 라이선스 안내 문구 번역 통일

import re
from KPC.classes import Error, BaseCheck

data = [
    {'msgid': 'Legal information\.',
     'msgstr': '법적 정보.'},
    {'msgid': 'As a special exception, the copyright holders give you ' +
              'permission to copy, modify, and distribute the example code ' +
              'contained  in this document under the terms of your ' +
              'choosing, without restriction.',
     'msgstr': '예외적으로, 이 문서에 들어 있는 예제 코드는 어떤 조건이든 제한 ' +
               '없이 복사, 수정, 배포할 수 있도록 저작권자가 특별히 허용합니다.'},
    {'msgid': 'This work is distributed under a CreativeCommons ' +
              'Attribution-Share Alike 3\.0 Unported license\.',
     'msgstr': '이 문서는 크리에이티브 커먼즈 저작자표시-동일조건변경허락 ' +
               '3.0 Unported 라이선스로 배포됩니다.'},
    {'msgid': 'Creative ?Commons Share ?Alike 3\.0',
     'msgstr': '크리에이티브 커먼즈 동일조건변경허락 3.0'},
    {'msgid': 'Creative ?Commons Share ?Alike 3\.0 United States License',
     'msgstr': '크리에이티브 커먼즈 동일조건변경허락 3.0 미합중국 라이선스'},
    {'msgid': 'Creative ?Commons Attribution-Share ?Alike 3\.0 United States ' +
              'License',
     'msgstr': '크리에이티브 커먼즈 저작자표시-동일조건변경허락 3.0 미합중국 라이선스'},
    {'msgid': 'Creative ?Commons Attribution-Share ?Alike 3\.0 Unported ' +
              'License',
     'msgstr': '크리에이티브 커먼즈 저작자표시-동일조건변경허락 3.0 Unported 라이선스'},
    {'msgid': '<em>To share</em>',
     'msgstr': '<em>공유</em>'},
    {'msgid': '<em>To remix</em>',
     'msgstr': '<em>변경</em>'},
    {'msgid': '<em>Attribution</em>',
     'msgstr': '<em>저작자 표시</em>'},
    {'msgid': '<em>Share Alike</em>',
     'msgstr': '"<em>동일 조건</em>'},
]


class HelpLicenseCheck(BaseCheck):
    errstr = '일관성을 위해 다음과 같이 번역합니다: %s'

    def check(self, entry, context):
        if True not in [('.page' in p or '.xml' in p) for p in entry.references]:
            return []
        for d in data:
            if not re.match(d['msgid'], entry.msgid, re.IGNORECASE):
                continue
            if entry.msgstr != d['msgstr']:
                return [Error(self.errstr % d['msgstr'])]
        return []

name = 'terminology/help-license'
description = '문서의 Creative Commons 라이선스 관련 번역이 통일된 번역인지 검사합니다'
checker = HelpLicenseCheck()
