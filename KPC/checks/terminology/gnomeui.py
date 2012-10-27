# -*- coding: utf-8 -*-
# terminology/gnomeui

# UI 나타나는 전형적인 단어들의 전형적인 번역 확인.  지정한 번역이
# 아니면 애러를 리턴한다.  번역 일관성 유지를 위한 검사.

import string
from KPC.classes import Error, BaseCheck

data = [('properties', '속성'),
        ('preferences', '기본 설정'),
        ('about', '정보'),
        ('find', '찾기'),
        ('search', '검색'),
        ('create', '만들기'),
        ('add', '추가'),
        ('remove', '제거'),
        ('edit', '편집'),
        ('view', '보기'),
        ('change', '바꾸기'),
        ('delete', '삭제'),
        ('exit', '끝내기'),
        ('log in', '로그인'),
        ('log out', '로그아웃'),
        ('run', '실행'),
        ('open', '열기'),
        ('save', '저장'),
        ('save as', '다른 이름으로 저장'),
        ('always on top', '항상 위'),
        ('previous', '이전'),
        ('next', '다음'),
        ('copy', '복사'),
        ('cut', '잘라내기'),
        ('paste', '붙여넣기'),
        ('location', '위치'),
        ('statusbar', '상태 표시줄'),
        ('zoom in', '확대'),
        ('zoom out', '축소'),
        ('browse', '찾아보기'),
        ('go', '이동'),
        ('name', '이름'),
        ('display', '표시'),
        ('clear', '지우기'),
        ('modify', '수정'),
        ('replace', '바꾸기'),
        ('template', '서식'),
        ('reload', '다시 읽기'),
        ('refresh', '새로 고침'),
        ('show', '보이기'),
        ('hide', '숨기기'),
        ('no', '아니요'),
        ]

def normalize_msgid(msgid):
    msgid = msgid.replace('_', '')
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
description = '지정한 그놈 데스크톱 용어로 번역했는지 검사합니다'
checker = GnomeUICheck()
