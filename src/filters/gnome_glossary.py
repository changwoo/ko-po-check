import string

name = "gnome-glossary"

data = [("properties", "등록 정보", "속성"),
        ("preferences", "기본 설정", "설정 사항"),
        ("preferences", "기본 설정", "환경설정"),
        ("about", "정보", "대하여"),
        ("font", "글꼴", "폰트"),
        ]
error_string = "%s: 그놈 데스크탑에서 \"%s\"은(는) \"%s\"(이)라고 번역"

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
