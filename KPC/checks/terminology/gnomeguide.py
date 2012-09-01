# -*- coding: utf-8 -*-

from KPC.classes import Error, BaseCheck

# 알파벳 순서대로 유지하세요
data = [
        ('about', u'정보', u'대하여'),
        ('application', u'프로그램', u'애플리케이션'),
        ('application', u'프로그램', u'어플리케이션'),
        ('background', u'배경', u'바탕'),
        ('button', u'단추', u'버튼'),
        ('change', u'바꾸기', u'변경'),
        ('clear', u'지우기', u'비우기'),
        ('clear', u'지우기', u'삭제'),
        ('create', u'만들기', u'생성'),
        ('data', u'데이터', u'데이타'),
        ('delete', u'삭제', u'지우기'),
        ('desktop', u'데스크톱', u'데스크탑'),
        ('desktop', u'바탕 화면', u'바탕화면'),
        ('directory', u'디렉터리', u'디렉토리'),
        ('download', u'다운로드', u'내려 받'),
        ('download', u'다운로드', u'내려받'),
        ('edit', u'편집', u'고치기'),
        ('exit', u'끝내기/마침', u'종료'),
        ('filename', u'파일 이름', u'파일명'),
        ('filename', u'파일 이름', u'파일이름'),
        ('filesystem', u'파일 시스템', u'파일시스템'),
        ('filter', u'필터', u'거르개'),
        ('filter', u'필터', u'거르게'),
        ('find', u'찾기', u'검색'),
        ('focus', u'포커스', u'초점'),
        ('font family', u'글꼴 계열', u'가족'),
        ('font family', u'글꼴 계열', u'패밀리'),
        ('font', u'글꼴', u'폰트'),
        ('game', u'게임', u'놀이'),
        ('graphics', u'그래픽', u'그래픽스'),
        ('graphics', u'그래픽', u'그림'),
        ('history', u'기록', u'히스토리'),
        ('hostname', u'호스트 이름', u'호스트명'),
        ('input method', u'입력기', u'입력 방법'),
        ('input method', u'입력기', u'입력 방식'),
        ('install',u'설치',u'깔기'),
        ('install',u'설치',u'인스톨'),
        ('item',u'항목',u'아이템'),
        ('key', u'키', u'글쇠'),
        ('keyboard', u'키보드', u'글쇠판'),
        ('launcher', u'실행 아이콘', u'실행기'),
        ('license', u'라이선스', u'라이센스'),
        ('link', u'링크', u'바로 가기'),
        ('link', u'링크', u'바로가기'),
        ('locale', u'로캘', u'로케일'),
        ('message', u'메시지', u'메세지'),
        ('modify', u'수정', u'고치'),
        ('modify', u'수정', u'바꾸'),
        ('non-free', u'독점', u'비자유'),
        ('password', u'암호', u'비밀 번호'),
        ('password', u'암호', u'비밀번호'),
        ('password', u'암호', u'열쇠글'),
        ('paste', u'붙여넣기', u'붙여 넣기'),
        ('preferences', u'기본 설정', u'기본설정'),
        ('preferences', u'기본 설정', u'선택 사항'),
        ('preferences', u'기본 설정', u'설정 사항'),
        ('preferences', u'기본 설정', u'환경설정'),
        ('properties', u'속성', u'등록 정보'),
        ('remember password', u'암호 저장', u'암호 기억'),
        ('remove', u'제거', u'삭제'),
        ('remove', u'제거', u'지우기'),
        ('replace', u'바꾸기', u'고치'),
        ('replace', u'바꾸기', u'대체'),
        ('replace', u'바꾸기', u'치환'),
        ('restart', u'다시 시작', u'재시작'),
        ('screensaver', u'화면 보호기', u'화면보호기'),
        ('search', u'검색', u'찾기'),
        ('separator', u'구분선', u'구분자'),
        ('shortcut', u'바로 가기', u'단축키'),
        ('shortcut', u'바로 가기', u'바로가기'),
        ('software',u'소프트웨어',u'무른모'),
        ('template', u'서식', u'템플리트'),
        ('template', u'서식', u'템플릿'),
        ('template', u'서식', u'틀'),
        ('update', u'업데이트', u'갱신'),
        ('username', u'사용자 이름', u'사용자명'),
        ('version', u'버전', u'버젼'),
        ('version', u'버전', u'판번호'),
        ]

class GnomeGuideCheck(BaseCheck):
    errstr = '%s: 그놈 데스크톱에서 \"%s\"은(는) \"%s\"(이)라고 번역'
    def check(self, entry):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        msgid_l = msgid.replace('_','').replace('&','').lower()
        for (id, right, wrong) in data:
            if (wrong in msgstr) and (id in msgid_l) and (not right in msgstr):
                errors.append(Error(self.errstr % (wrong, id, right)))
        return errors

name = 'terminology/gnomeguide'
description = '잘못 번역된 그놈 데스크톱 용어를 검사합니다'
checker = GnomeGuideCheck()
