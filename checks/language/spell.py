#!/usr/bin/python

import string,re

name = "common-misspell"

e = lambda s: unicode(s,'utf-8')

# 의존명사를 위한 -할 형태의 동사 모음
verbs_re = "("+string.join([
    "가져올",
    "갈",
    "걸",
    "고칠"
    "나타날",
    "내릴",
    "놓일",
    "되돌릴",
    "만들",
    "바꿀",
    "보낼",
    "볼",
    "생길",
    "시킬",
    "쓸",
    "알",
    "얻어낼",
    "얻을",
    "없앨",
    "열",
    "올",
    "일",
    "읽어들일",
    "읽을",
    "있을",
    "잠글",
    "지울",
    "찾을",
    "할",
    ], '|')+")"

variations_re = "(있다|없다|있습니다|없습니다|있는|없는|있게|없게)"

# 조사 모음
chosa_re = "("+string.join([
    '가','이','이\(가\)',
    '를','을','을\(를\)',
    '는','은','은\(는\)',
    '로','으로','\(으\)로',
    '로서','으로서','\(으\)로서',
    '로써','으로써','\(으\)로써',
    '로부터','으로부터','\(으\)로부터',
    '라는','이라는','\(이\)라는',
    '의', '도', '에', '에서', '만', '부터',
    ], '|')+")"

def test_noun_suffix(str):
    if (str[-1] != e('슴')):
        return 1
    elif ((ord(str[-2]) - 0xac00) % 28 == 20):
        return 0
    elif (str[-2] == e('없')):
        return 0
    else:
        return 1
    

misspell_data = [
    { 're':    re.compile(e("(않\s*(한|함|합니다|된|됨|됩니다))")),
      'error': e("\"%s\": 짧은 부정문에서는 '않'이 아니라 '안'을 씁니다") },
    { 're':    re.compile(e("(읍니다)")),
      'error': e("\"%s\": '읍니다'가 아니라 '습니다'입니다") },
    { 're':    re.compile(e("([^\s]+슴)([\s\.\,\?]|$)")),
      'func':  test_noun_suffix,
      'error': e("\"%s\": '슴'이 아니라 '음'입니다") },
    { 're':    re.compile(e("("+verbs_re+"수(가|도|는)?\s"+")")),
      'error': e("\"%s\": 의존 명사는 띄어 써야 합니다") },
    { 're':    re.compile(e("("+verbs_re+"\s*수(있|없)"+")")),
      'error': e("\"%s\": 의존 명사는 띄어 써야 합니다") },
    { 're':    re.compile(e("("+verbs_re+"때(가|도|는)?\s"+")")),
      'error': e("\"%s\": `~할 때'라고 띄어 써야 합니다") },
    { 're':    re.compile(e("([0-9A-Za-z-+`'\"()%_]+ "+chosa_re+")\s+")),
      'error': e("\"%s\": 조사는 체언에 붙여 써야 합니다") },
]

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    for data in misspell_data:
        misspell_re = data['re']
        misspell_error = data['error']
        str = msgstr
        while 1:
            mo = misspell_re.search(str)
            if mo:
                if (data.has_key('func') and data['func'](mo.group(1))):
                    str = str[mo.end():]
                    continue
                ret = 0
                if errmsg:
                    errmsg += '\n'
                errmsg += misspell_error % mo.group(1)
                str = str[mo.end():]
            else:
                break;
    return (ret, errmsg)    

if __name__ == '__main__':
    import sys
    msgid = unicode(sys.stdin.readline(),'euckr')
    msgstr = unicode(sys.stdin.readline(),'euckr')
    t,e = check(msgid,msgstr)
    if not t:
        print e.encode('euckr')
    else:
        print "Success"

# Local Variables:
# coding: utf-8
# End:
