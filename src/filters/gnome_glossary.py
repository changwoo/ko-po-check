import string

name = "gnome-glossary"

import localeutil
e = localeutil.eucstr

data = [("properties", e("등록 정보"), e("속성")),
        ("preferences", e("기본 설정"), e("설정 사항")),
        ("preferences", e("기본 설정"), e("선택 사항")),
        ("preferences", e("기본 설정"), e("환경설정")),
        ("about", e("정보"), e("대하여")),
        ("font", e("글꼴"), e("폰트")),
        ("button", e("단추"), e("버튼")),
        ("delete", e("지우기"), e("삭제")),
        ("find", e("찾기"), e("검색")),
        ("search", e("찾기"), e("검색")),
        ("create", e("만들기"), e("생성")),
        ("add", e("더하기"), e("추가")),
        ("change", e("바꾸기"), e("변경")),
        ("remove", e("지우기"), e("제거")),
        ("exit", e("끝내기/마침"), e("종료")),
        ("background", e("바탕색"), e("배경")),
        ("foreground", e("글자색"), e("전경")),
        ("display", e("보여주기"), e("표시")),
        ("application", e("프로그램"), e("어플리케이션")),
        ]

error_string = e("%s: 그놈 데스크탑에서 \"%s\"은(는) \"%s\"(이)라고 번역")

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
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
        print "Success"
