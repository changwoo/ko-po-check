#!/usr/bin/python

import re,string

name = "should-have-chosa-alternative"

e = lambda s: unicode(s,'utf-8')

chosa_data = [(e('가'),e('이'),e('이(가)')),
              (e('를'),e('을'),e('을(를)')),
              (e('는'),e('은'),e('은(는)')),
              (e('로'),e('으로'),e('(으)로')),
              (e('로서'),e('으로서'),e('(으)로서')),
              (e('로써'),e('으로써'),e('(으)로써')),
              (e('로부터'),e('으로부터'),e('(으)로부터')),
              (e('라는'),e('이라는'),e('(이)라는'))]

def chosa_suggest(cho):
    for (a,b,s) in chosa_data:
        if cho == a or cho == b:
            return s
    return '????'

format = "%([1-9][0-9]*\$)?[-+ #'0]*([1-9][0-9]*)?(\.[0-9]+)?((hh|h|j|l|L|ll|q|t|z|Z)?[dioufeEgGaAcCspnmhjlLqtxXzZ1-9]|hh|ll)"
chosa = "(" + string.join(map(lambda p: p[0]+"|"+p[1], chosa_data),'|') + ")"

chosa_re = re.compile("(("+format+"['\"]?) ?"+chosa+")(\s|$)")
error_string = e("\"%s\": 받침에 따른 조사 구별이 없습니다. '%s'")

def check(msgid,msgstr):
    ret = 1
    errmsg = ""
    while 1:
        mo = chosa_re.search(msgstr)
        if mo and (mo.end() >= len(msgstr) or msgstr[mo.end()] != '('):
            ret = 0
            if errmsg:
                errmsg += '\n'
            sug = mo.group(2) + chosa_suggest(mo.group(8))
            errmsg += error_string % (mo.group(1),sug)
            msgstr = msgstr[mo.end():]
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

# Local Variables:
# coding: utf-8
# End:

