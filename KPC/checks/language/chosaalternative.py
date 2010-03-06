# -*- coding: utf-8 -*-

import re,string
from KPC.classes import Error, BaseCheck

chosa_data = [(u'가',u'이',u'이(가)'),
              (u'를',u'을',u'을(를)'),
              (u'는',u'은',u'은(는)'),
              (u'로',u'으로',u'(으)로'),
              (u'로서',u'으로서',u'(으)로서'),
              (u'로써',u'으로써',u'(으)로써'),
              (u'로부터',u'으로부터',u'(으)로부터'),
              (u'라는',u'이라는',u'(이)라는')]
format = '%([1-9][0-9]*\$)?[-+ #\'0]*([1-9][0-9]*)?(\.[0-9]+)?((hh|h|j|l|L|ll|q|t|z|Z)?[dioufeEgGaAcCspnmhjlLqtxXzZ1-9]|hh|ll)'
chosa = '(' + string.join(map(lambda p: p[0]+'|'+p[1], chosa_data),'|') + ')'
chosa_re = re.compile('(('+format+'[\'\"]?) ?'+chosa+')(\s|$)')

def chosa_suggest(cho):
    for (a,b,s) in chosa_data:
        if cho == a or cho == b:
            return s
    return '????'

class ChosaAlternativeCheck(BaseCheck):
    errstr = '\"%s\": 받침에 따른 조사 구별이 없습니다. \'%s\''
    def check(self, entry):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        while True:
            mo = chosa_re.search(msgstr)
            if mo and (mo.end() >= len(msgstr) or msgstr[mo.end()] != '('):
                sug = mo.group(2) + chosa_suggest(mo.group(8))
                errors.append(Error(self.errstr % (mo.group(1), sug)))
                msgstr = msgstr[mo.end():]
            else:
                break;
        return errors

name = 'language/chosa-alternative'
description = '조사 구분을 했는지 검사합니다'
checker = ChosaAlternativeCheck()
