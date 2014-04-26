# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

err_fmt = '검색어 번역은 \';\'으로 끝나야 합니다'
err_org = '%s: 검색어 번역에는 원문 키워드를 포함해야 합니다'
err_dup = '%s: 검색어가 중복되어 있습니다'

re_keyword = re.compile(r'^(?:[\w ]+;)+$')


class DesktopKeywordCheck(BaseCheck):
    def is_keyword(self, entry):
        if not True in [('.desktop' in p) for p in entry.references]:
            return False
        return re_keyword.match(entry.msgid)

    def check(self, entry, context):
        if not self.is_keyword(entry):
            return []
        msgid_keywords = entry.msgid[:-1].split(';')
        if entry.msgstr[-1] != ';':
            return [Error(err_fmt)]
        msgstr_keywords = entry.msgstr[:-1].split(';')
        for k in msgid_keywords:
            if not k in msgstr_keywords:
                return [Error(err_org % k)]
        s = set()
        for k in msgstr_keywords:
            if k in s:
                return [Error(err_dup % k)]
            s.add(k)
        return []


name = 'convention/desktop-keyword'
description = 'freedesktop.org desktop 엔트리의 Keyword 번역을 확인합니다'
checker = DesktopKeywordCheck()
