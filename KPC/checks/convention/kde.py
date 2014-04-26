# -*- coding: utf-8 -*-
# KDE specific rule

from KPC.classes import Error, BaseCheck


class KDECheck(BaseCheck):
    name_error = Error('KDE 번역 규칙에 따라 번역자 이름을 써야 합니다')
    email_error = Error('KDE 번역 규칙에 따라 번역자 메일 주소를 써야 합니다')

    def check(self, entry, context):
        msgstr = entry.msgstr
        msgctxt = entry.msgctxt
        if msgctxt == 'NAME OF TRANSLATORS':
            # msgid "Your names"
            if '이름' in msgstr or '성함' in msgstr:
                return [self.name_error]
        elif msgctxt == 'EMAIL OF TRANSLATORS':
            # msgid "Your emails"
            if '메일' in msgstr or '편지' in msgstr:
                return [self.email_error]
        return []


name = 'convention/kde'
description = 'KDE 프로젝트에서 사용하는 관행에 맞는지 검사합니다'
checker = KDECheck()
