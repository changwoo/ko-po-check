# -*- coding: utf-8 -*-
# terminology/desktop-commons

# UI 나타나는 전형적인 단어들의 전형적인 번역 확인.  지정한 번역이
# 아니면 애러를 리턴한다.  번역 일관성 유지를 위한 검사.

from KPC.classes import Error, BaseCheck

data = [
    ('about', '정보'),
    ('add', '추가'),
    ('always on top', '항상 위'),
    ('browse', '찾아보기'),
    ('change', '바꾸기'),
    ('clear', '지우기'),
    ('copy', '복사'),
    ('create', '만들기'),
    ('cut', '잘라내기'),
    ('delete', '삭제'),
    ('display', '표시'),
    ('edit', '편집'),
    ('exit', '나가기'),
    ('find', '찾기'),
    ('go', '이동'),
    ('hide', '숨기기'),
    ('location', '위치'),
    ('log in', '로그인'),
    ('log out', '로그아웃'),
    ('modify', '수정'),
    ('name', '이름'),
    ('next', '다음'),
    ('no', '아니요'),
    ('open', '열기'),
    ('paste', '붙여넣기'),
    ('preferences', '기본 설정'),
    ('previous', '이전'),
    ('properties', '속성'),
    ('quit', '끝내기'),
    ('refresh', '새로 고침'),
    ('reload', '다시 읽기'),
    ('remove', '제거'),
    ('replace', '바꾸기'),
    ('run', '실행'),
    ('save as', '다른 이름으로 저장'),
    ('save', '저장'),
    ('search', '검색'),
    ('show', '보이기'),
    ('statusbar', '상태 표시줄'),
    ('template', '서식'),
    ('view', '보기'),
    ('zoom in', '확대'),
    ('zoom out', '축소'),
]


def normalize_msgid(msgid):
    msgid = msgid.replace('_', '')
    if msgid[-3:] == '...':
        msgid = msgid[:-3]
    return msgid


def make_msgstr(msgstr, mnemonic, dots):
    if mnemonic:
        msgstr = msgstr + '(_' + mnemonic + ')'
    if dots:
        msgstr = msgstr + '...'
    return msgstr


def find_mnemonic(msgid):
    try:
        i = msgid.index('_')
        return msgid[i+1].upper()
    except ValueError:
        return None


class DesktopCommonsCheck(BaseCheck):
    errstr = '%s: 다음과 같이 번역해야 합니다: \"%s\"'

    def check(self, entry, context):
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

name = 'terminology/desktop-commons'
description = '많이 사용되는 데스크톱 용어를 일관적으로 번역했는지 검사합니다'
checker = DesktopCommonsCheck()
