# terminology/gnomeui

# UI 나타나는 전형적인 단어들의 전형적인 번역 확인.  지정한 번역이
# 아니면 애러를 리턴한다.  번역 일관성 유지를 위한 검사.

import string

name = "terminology/gnomeui"

e = lambda s: unicode(s,'utf-8')

data = [("properties", e("등록 정보")),
        ("preferences", e("기본 설정")),
        ("about", e("정보")),
        ("find", e("찾기")),
        ("search", e("찾기")),
        ("create", e("만들기")),
        ("add", e("더하기")),
        ("edit", e("편집")),
        ("view", e("보기")),
        ("change", e("바꾸기")),
        ("remove", e("지우기")),
        ("exit", e("끝내기")),
        ("log in", e("로그인")),
        ("log out", e("로그아웃")),
        ("run", e("실행")),
        ("open", e("열기")),
        ("save", e("저장")),
        ("save as", e("다른 이름으로 저장")),
        ("always on top", e("항상 위")),
        ("previous", e("이전")),
        ("next", e("다음")),
        ("copy", e("복사")),
        ("cut", e("잘라내기")),
        ("paste", e("붙여 넣기")),
        ("location", e("위치")),
        ("statusbar", e("상태 표시줄")),
        ("zoom in", e("확대")),
        ("zoom out", e("축소")),
        ("browse", e("찾아보기")),
        ("go", e("이동")),
        ]

error_string = e("%s: 다음과 같이 번역해야 합니다: \"%s\"")


def normalize_msgid(msgid):
    msgid = string.replace(msgid, '_', '')
    if msgid[-3:] == '...':
        msgid = msgid[:-3]
    return string.lower(msgid)

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
    
def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    msgid_n = normalize_msgid(msgid)
    msgid_m = find_mnemonic(msgid)
    msgid_d = (msgid[-3:] == '...')
    for (orig, trans) in data:
        if msgid_n == orig:
            good_msgstr = make_msgstr(trans, msgid_m, msgid_d)
            if good_msgstr != msgstr:
                ret = 0
                if errmsg:
                    errmsg += '\n'
                errmsg += error_string % (msgstr, good_msgstr)
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

# Local Variables:
# coding: utf-8
# End:
