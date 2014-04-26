# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

josa_data = [('가', '이', '이(가)'),
             ('를', '을', '을(를)'),
             ('는', '은', '은(는)'),
             ('와', '과', '과(와)'),
             ('로', '으로', '(으)로'),
             ('로서', '으로서', '(으)로서'),
             ('로써', '으로써', '(으)로써'),
             ('로부터', '으로부터', '(으)로부터'),
             ('라는', '이라는', '(이)라는')]
c_format = '%(?:[1-9][0-9]*\$)?[-+ #\'0]*(?:[1-9][0-9]*)?(?:\.[0-9]+)?' \
           '(?:(?:hh|h|j|l|L|ll|q|t|z|Z)?' \
           '[dioufeEgGaAcCspnmhjlLqtxXzZ1-9]|hh|ll)'
py_format = '%(?:\([A-Za-z]\w+\))?[#-0\ +]*(?:[0-9]+|\*)?(?:\.[0-9]+)?' \
            '[hlL]?[diouxXeEfFgGcrs]'

josa = '(?:' + '|'.join([p[0]+'|'+p[1] for p in josa_data]) + ')'
josa_c_re = re.compile('(?P<case>(?P<fmt>'+c_format+'[\'\"]?) ?'
                       '(?P<josa>'+josa+'))(?:\s|$)')
josa_py_re = re.compile('(?P<case>(?P<fmt>'+py_format+'[\'\"]?) ?'
                        '(?P<josa>'+josa+'))(?:\s|$)')


def josa_suggest(cho):
    for (a, b, s) in josa_data:
        if cho == a or cho == b:
            return s
    return '????'


class JosaAlternativeCheck(BaseCheck):
    errstr = '\"%s\": 받침에 따른 조사 구별이 없습니다. \'%s\''

    def check(self, entry, context):
        if entry.is_c_format():
            josa_re = josa_c_re
        elif entry.is_python_format():
            josa_re = josa_py_re
        else:
            return []
        msgstr = entry.msgstr
        errors = []
        while True:
            mo = josa_re.search(msgstr)
            if mo:
                sug = mo.group('fmt') + josa_suggest(mo.group('josa'))
                errors.append(Error(self.errstr % (mo.group('case'), sug)))
                msgstr = msgstr[mo.end():]
            else:
                break
        return errors

name = 'language/josa-alternative'
description = '조사 구분을 했는지 검사합니다'
checker = JosaAlternativeCheck()
