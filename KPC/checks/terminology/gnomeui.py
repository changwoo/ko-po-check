# -*- coding: utf-8 -*-
# terminology/gnomeui

# UI 나타나는 전형적인 단어들의 전형적인 번역 확인.  지정한 번역이
# 아니면 애러를 리턴한다.  번역 일관성 유지를 위한 검사.

import string
from KPC.classes import Error, BaseCheck

data = [('properties', u'속성'),
        ('preferences', u'기본 설정'),
        ('about', u'정보'),
        ('find', u'찾기'),
        ('search', u'검색'),
        ('create', u'만들기'),
        ('add', u'추가'),
        ('remove', u'제거'),
        ('edit', u'편집'),
        ('view', u'보기'),
        ('change', u'바꾸기'),
        ('delete', u'삭제'),
        ('exit', u'끝내기'),
        ('log in', u'로그인'),
        ('log out', u'로그아웃'),
        ('run', u'실행'),
        ('open', u'열기'),
        ('save', u'저장'),
        ('save as', u'다른 이름으로 저장'),
        ('always on top', u'항상 위'),
        ('previous', u'이전'),
        ('next', u'다음'),
        ('copy', u'복사'),
        ('cut', u'잘라내기'),
        ('paste', u'붙여넣기'),
        ('location', u'위치'),
        ('statusbar', u'상태 표시줄'),
        ('zoom in', u'확대'),
        ('zoom out', u'축소'),
        ('browse', u'찾아보기'),
        ('go', u'이동'),
        ('name', u'이름'),
        ('display', u'표시'),
        ('clear', u'지우기'),
        ('modify', u'수정'),
        ('replace', u'바꾸기'),
        ('template', u'서식'),
        ('reload', u'다시 읽기'),
        ('refresh', u'새로 고침'),
        ('show', u'보이기'),
        ('hide', u'숨기기'),
        ('no', u'아니요'),
        ]

def normalize_msgid(msgid):
    msgid = string.replace(msgid, '_', '')
    if msgid[-3:] == '...':
        msgid = msgid[:-3]
    return msgid

def make_msgstr(msgstr,mnemonic,dots):
    if mnemonic:
        msgstr = msgstr + '(_' + mnemonic + ')'
    if dots:
        msgstr = msgstr + '...'
    return msgstr

def find_mnemonic(msgid):
    try:
        i = string.index(msgid,'_')
        return string.upper(msgid[i+1])
    except:
        return None
    
class GnomeUICheck(BaseCheck):
    errstr = '%s: 다음과 같이 번역해야 합니다: \"%s\"'

    def check(self, entry):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        msgid_n = normalize_msgid(msgid)
        msgid_m = find_mnemonic(msgid)
        msgid_d = (msgid[-3:] == '...')
        for (orig, trans) in data:
            # 모두 대문자로 된 단어는 option argument 따위로 쓰이므로 넘어간다
            if msgid_n.lower() == orig and not msgid_n.isupper():
                good_msgstr = make_msgstr(trans, msgid_m, msgid_d)
                if good_msgstr != msgstr:
                    errors.append(Error(self.errstr % (msgstr, good_msgstr)))
        return errors

name = 'terminology/gnomeui'
description = '지정한 그놈 데스크탑 용어로 번역했는지 검사합니다'
checker = GnomeUICheck()
