# -*- coding: utf-8 -*-

from KPC.classes import Error, BaseCheck

# 알파벳 순서대로 유지하세요
data = [
    ('about', '정보', '대하여'),
    ('application', '프로그램', '애플리케이션'),
    ('application', '프로그램', '어플리케이션'),
    ('background', '배경', '바탕'),
    ('button', '단추', '버튼'),
    ('change', '바꾸기', '변경'),
    ('center', '센타', '센터'),
    ('clear', '지우기', '비우기'),
    ('clear', '지우기', '삭제'),
    ('create', '만들기', '생성'),
    ('data', '데이터', '데이타'),
    ('debug', '디버깅', '디버그'),
    ('delete', '삭제', '지우기'),
    ('desktop', '데스크톱', '데스크탑'),
    ('desktop', '바탕 화면', '바탕화면'),
    ('directory', '디렉터리', '디렉토리'),
    ('download', '다운로드', '내려 받'),
    ('download', '다운로드', '내려받'),
    ('edit', '편집', '고치기'),
    ('exit', '나가기', '종료'),
    ('filename', '파일 이름', '파일명'),
    ('filename', '파일 이름', '파일이름'),
    ('filesystem', '파일 시스템', '파일시스템'),
    ('filter', '필터', '거르개'),
    ('filter', '필터', '거르게'),
    ('find', '찾기', '검색'),
    ('focus', '포커스', '초점'),
    ('font family', '글꼴 계열', '가족'),
    ('font family', '글꼴 계열', '패밀리'),
    ('font', '글꼴', '폰트'),
    ('game', '게임', '놀이'),
    ('graphics', '그래픽', '그래픽스'),
    ('graphics', '그래픽', '그림'),
    ('history', '기록', '히스토리'),
    ('hostname', '호스트 이름', '호스트명'),
    ('input method', '입력기', '입력 방법'),
    ('input method', '입력기', '입력 방식'),
    ('install', '설치', '깔기'),
    ('install', '설치', '인스톨'),
    ('item', '항목', '아이템'),
    ('key', '키', '글쇠'),
    ('keyboard', '키보드', '글쇠판'),
    ('launcher', '실행 아이콘', '실행기'),
    ('license', '라이선스', '라이센스'),
    ('link', '링크', '바로 가기'),
    ('link', '링크', '바로가기'),
    ('locale', '로캘', '로케일'),
    ('e-mail', '전자메일', '이메일'),
    ('email', '전자메일', '이메일'),
    ('message', '메시지', '메세지'),
    ('modify', '수정', '고치'),
    ('modify', '수정', '바꾸'),
    ('non-free', '독점', '비자유'),
    ('password', '암호', '비밀 번호'),
    ('password', '암호', '비밀번호'),
    ('password', '암호', '열쇠글'),
    ('paste', '붙여넣기', '붙여 넣기'),
    ('preferences', '기본 설정', '기본설정'),
    ('preferences', '기본 설정', '선택 사항'),
    ('preferences', '기본 설정', '설정 사항'),
    ('preferences', '기본 설정', '환경설정'),
    ('properties', '속성', '등록 정보'),
    ('remember password', '암호 저장', '암호 기억'),
    ('remove', '제거', '삭제'),
    ('remove', '제거', '지우기'),
    ('replace', '바꾸기', '고치'),
    ('replace', '바꾸기', '대체'),
    ('replace', '바꾸기', '치환'),
    ('restart', '다시 시작', '재시작'),
    ('screensaver', '화면 보호기', '화면보호기'),
    ('search', '검색', '찾기'),
    ('separator', '구분선', '구분자'),
    ('shortcut', '바로 가기', '단축키'),
    ('shortcut', '바로 가기', '바로가기'),
    ('software', '소프트웨어', '무른모'),
    ('tablet', '태블릿', '타블렛'),
    ('template', '서식', '템플리트'),
    ('template', '서식', '템플릿'),
    ('template', '서식', '틀'),
    ('thread', '스레드', '쓰레드'),
    ('update', '업데이트', '갱신'),
    ('username', '사용자 이름', '사용자명'),
    ('version', '버전', '버젼'),
    ('version', '버전', '판번호'),
    ('vimeo', '비미오', '비메오'),
    ('youtube', '유튜브', '유투브'),
    ('windows', '윈도우', '윈도우즈'),
]


class WordGuideCheck(BaseCheck):
    errstr = '%s: \"%s\"은(는) \"%s\"(이)라고 번역하길 제안합니다'

    def check(self, entry, context):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        msgid_l = msgid.replace('_', '').replace('&', '').lower()
        for (id, right, wrong) in data:
            if not (wrong in msgstr) or not (id in msgid_l):
                continue
            if not right in wrong and right in msgstr:
                continue
            errors.append(Error(self.errstr % (wrong, id, right.strip())))
        return errors

name = 'terminology/word-guide'
description = '바람직하지 않은 번역 용어를 검사합니다'
checker = WordGuideCheck()
