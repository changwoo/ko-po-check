# -*- coding: utf-8 -*-
# 헤더 코멘트 검사

import string
from KPC.classes import Error, BaseCheck

class HeaderCommentCheck(BaseCheck):
    def check(self, entry):
        if entry.msgid != '':
            return []
        fields = {}
        for line in entry.msgstr.split('\n'):
            try:
                k, v = line.split(': ', 1)
                fields[k] = v
            except ValueError:
                pass
        errors = []
        # PO-Revision-Date의 연도에 맞게 코멘트의 연도가 업데이트되었는지 확인
        try:
            name = fields['Last-Translator'].split(' <')[0]
            year = fields['PO-Revision-Date'][:4]
        except IndexError:
            # FIXME: PO-Revision-Date 또는 Last-Translator가 포맷에 맞지 않는 경우, 또 다른 에러 출력?
            pass
        for line in entry.translator_comment.split('\n'):
            if name in line and year in line:
                break
        else:
            errors.append(Error('헤더 코멘트에 %s 번역자의 %s년도 기록이 없습니다' % (name, year)))
        return errors
        

name = 'convention/header-comment'
description = '헤더 코멘트가 올바른지 검사합니다'
checker = HeaderCommentCheck()
