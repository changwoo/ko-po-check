#!/usr/bin/python

import string,re

name = "common-misspell"

def euc(s):
    return unicode(s,'euc-kr').encode('utf-8')

# 의존명사를 위한 -할 형태의 동사 모음
verbs_re = "("+string.join([
    "가져올",
    "고칠"
    "나타날",
    "놓일",
    "되돌릴",
    "만들",
    "바꿀",
    "볼",
    "쓸",
    "알"
    "얻을",
    "열",
    "읽어들일",
    "읽을",
    "있을",
    "지울",
    "찾을",
    "할",
    ], '|')+")"

variations_re = "(있다|없다|있습니다|없습니다|있는|없는|있게|없게)"

misspell_data = [
    { 're':    re.compile(euc("(않\s*(한|함|합니다|된|됨|됩니다))")),
      'error': euc("\"%s\": 짧은 부정문에서는 '않'이 아니라 '안'을 씁니다") },
    { 're':    re.compile(euc("(읍니다)")),
      'error': euc("\"%s\": '읍니다'가 아니라 '습니다'입니다") },
    { 're':    re.compile(euc("((없|있|남았)슴)")),
      'error': euc("\"%s\": '슴'이 아니라 '음'입니다") },
    { 're':    re.compile(euc("("+verbs_re+"수(가|도|는)?\s"+")")),
      'error': euc("\"%s\": 의존 명사는 띄어 써야 합니다") },
    { 're':    re.compile(euc("("+verbs_re+"\s*수(있|없)"+")")),
      'error': euc("\"%s\": 의존 명사는 띄어 써야 합니다") },
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
                ret = 0
                if errmsg:
                    errmsg += '\n'
                errmsg += misspell_error % str[mo.start(1):mo.end(1)]
                str = str[mo.end():]
            else:
                break;
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
