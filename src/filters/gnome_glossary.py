import string

name = "gnome-glossary"

import localeutil
e = localeutil.eucstr

data = [("properties", e("등록 정보"), e("속성")),
        ("preferences", e("기본 설정"), e("설정 사항")),
        ("preferences", e("기본 설정"), e("환경설정")),
        ("about", e("정보"), e("대하여")),
        ("font", e("글꼴"), e("폰트")),
        ]

error_string = e("%s: 그놈 데스크탑에서 \"%s\"은(는) \"%s\"(이)라고 번역")

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    for (id, right, wrong) in data:
        if ((string.find(msgstr, wrong) >= 0) and
            (string.find(string.lower(msgid), id) >= 0) and
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
