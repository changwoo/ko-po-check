# -*- coding: utf-8 -*-
import string

name = 'terminology/gnomeguide'

data = [('properties', u'속성', u'등록 정보'),
        ('preferences', u'기본 설정', u'설정 사항'),
        ('preferences', u'기본 설정', u'선택 사항'),
        ('preferences', u'기본 설정', u'환경설정'),
        ('preferences', u'기본 설정', u'기본설정'),
        ('about', u'정보', u'대하여'),
        ('font', u'글꼴', u'폰트'),
        ('button', u'단추', u'버튼'),
        ('delete', u'지우기', u'삭제'),
        ('find', u'찾기', u'검색'),
        ('search', u'찾기', u'검색'),
        ('create', u'만들기', u'생성'),
        ('add', u'더하기', u'추가'),
        ('change', u'바꾸기', u'변경'),
        ('remove', u'지우기', u'제거'),
        ('exit', u'끝내기/마침', u'종료'),
        ('background', u'바탕색', u'배경'),
        ('foreground', u'글자색', u'전경'),
        ('application', u'프로그램', u'어플리케이션'),
        ('application', u'프로그램', u'애플리케이션'),
        ('key', u'키', u'글쇠'),
        ('translator', u'옮긴이', u'번역자'),
        ('password', u'암호', u'열쇠글'),
        ('password', u'암호', u'비밀번호'),
        ('password', u'암호', u'비밀 번호'),
        ('paste', u'붙여 넣기', u'붙여넣기'),
        ('focus', u'포커스', u'초점'),
        ('restart', u'다시 시작', u'재시작'),
        ('screensaver', u'화면 보호기', u'화면보호기'),
        ('link', u'링크', u'바로 가기'),
        ('link', u'링크', u'바로가기'),
        ('graphics', u'그래픽', u'그림'),
        ('graphics', u'그래픽', u'그래픽스'),
        ('shortcut', u'바로 가기', u'바로가기'),
        ('shortcut', u'바로 가기', u'단축키'),
        ]

error_string = u'%s: 그놈 데스크탑에서 \"%s\"은(는) \"%s\"(이)라고 번역'

def check(msgid,msgstr):
    ret = 1
    errmsg = ''
    msgid_l = string.lower(string.replace(string.replace(msgid,'_',''),'&',''))
    for (id, right, wrong) in data:
        if ((string.find(msgstr, wrong) >= 0) and
            (string.find(msgid_l, id) >= 0) and
            (string.find(msgstr, right) < 0)):
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += error_string % (wrong, id, right)
    return (ret, errmsg)    

if __name__ == '__main__':
    import sys
    msgid = sys.stdin.readline()
    msgstr = sys.stdin.readline()
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print 'Success'

# Local Variables:
# coding: utf-8
# End:
