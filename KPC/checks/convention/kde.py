# -*- coding: utf-8 -*-
# KDE specific rule

name = 'convention/kde'
description = 'KDE 프로젝트에서 사용하는 관행에 맞는지 검사합니다'

name_error_str = u'KDE 번역 규칙에 따라 번역자 이름을 써야 합니다.'
email_error_str = u'KDE 번역 규칙에 따라 번역자 메일 주소를 써야 합니다.'

import string

def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    msgctxt = entry.msgctxt
    if msgctxt == "NAME OF TRANSLATORS":
        # msgid "Your names"
        if (msgstr.find(u'이름') >= 0 or msgstr.find(u'성함') >= 0):
            return (0, name_error_str)
    elif msgctxt == "EMAIL OF TRANSLATORS":
        # msgid "Your emails"
        if (msgstr.find(u'메일') >= 0 or msgstr.find(u'편지') >= 0):
            return (0, email_error_str)
    return (1,'')
