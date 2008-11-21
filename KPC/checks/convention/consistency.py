# -*- coding: utf-8 -*-

import re

name = "convention/consistency"
description = "번역문이 원문과 비슷한 문장 부호로 끝나도록 합니다"

data = [
    { 're': re.compile(".*[^\.]\.$"),
      'error':  u'번역문이 원문과 같이 .으로 끝나야 합니다' },
    { 're': re.compile(".*:$"),
      'error':  u'번역문이 원문과 같이 :으로 끝나야 합니다' },
    { 're': re.compile(".*\.\.\.$"),
      'error':  u'번역문이 원문과 같이 ...으로 끝나야 합니다' },
    ]
    
def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    ret = 1
    errmsg = ""
    for d in data:
        re = d['re']
        error = d['error']
        if re.match(msgid) and not re.match(msgstr):
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += error
    return (ret, errmsg)    

if __name__ == '__main__':
    import sys
    msgid = unicode(sys.stdin.readline(),'utf8')
    msgstr = unicode(sys.stdin.readline(),'utf8')
    t,e = check(msgid,msgstr)
    if not t:
        print e.encode('utf8')
    else:
        print 'Success'
