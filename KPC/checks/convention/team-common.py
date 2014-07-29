# -*- coding: utf-8 -*-

from KPC.classes import Error, HeaderCheck, CheckList

class NoPoliticsCheck(HeaderCheck):
    keywords = ['dokdo']
    errmsg = '정치적 문구를 쓰는 곳이 아닙니다: %s'

    def check_header(self, entry, fields):
        comment_lines = entry.translator_comment.split('\n')
        r = []
        for k in self.keywords:
            try:
                if k in fields['Last-Translator'].lower():
                    r.append(Error(self.errmsg % fields['Last-Translator']))
                if k in fields['Language-Team'].lower():
                    r.append(Error(self.errmsg % fields['Language-Team']))
                for l in comment_lines:
                    if k in l.lower():
                        r.append(Error(self.errmsg % l))
            except KeyError:
                pass
        return r


name = 'convention/team-common'
description = '번역팀 공통 관련 사항을 검사합니다'
checker = CheckList([NoPoliticsCheck()])
