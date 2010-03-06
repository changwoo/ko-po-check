# -*- coding: utf-8 -*-

import re, string
from KPC.classes import Error, BaseCheck

gnome_mnemonic_re = re.compile('^[^_]*_([0-9A-Za-z])[^_]*$')
kde_mnemonic_re = re.compile('^[^_]*&([0-9A-Za-z])[^_]*$')


re_mnemonic = re.compile('^[^_]*[_&]([0-9A-Za-z])[^_]*$')

# 예외적인 경우:
# "abc_DEF" 등 중간에 밑줄 다음에 대문자가 나오는 경우
# &amp; intltool에서 XML에서 변환하면서 unescape되지 않은 몇몇 케이스
re_mnemonic_unlikely = re.compile('(^[^_]*[a-zA-Z]_[A-Z][^_]*$.*%[ds].*)')

errstr_no_mnemonic = u'번역문에 접근키가 없거나 두 개 이상입니다'
errstr_wrong = u'\'%s\' vs \'%s\': 원문과 번역문의 접근키가 다릅니다'

re_lowercase_mnemonic = re.compile('(\([_&][a-z]\))')
errstr_lowercase = u'\"%s\": 접근키가 소문자입니다'

class AccessKeyCheck(BaseCheck):
    def check(self, entry):
        msgid = entry.msgid
        msgstr = entry.msgstr
        mo = re_mnemonic.match(msgid)
        if mo:
            # doubts if the string really contains a mnemonic
            if re_mnemonic_unlikely.match(msgid):
                return []
            # too long string to be a label string
            if len(msgid) > 60:
                return []
            # GNOME schema file
            if entry.references and entry.references[0].find('.schemas') >= 0:
                return []
            
            letter = string.upper(mo.group(1))
            # check 1: if it's translated with the mnemonic
            mo = re_mnemonic.match(msgstr)
            if not mo:
                return [Error(errstr_no_mnemonic)]

            # check 2: check if it's same
            if letter != string.upper(mo.group(1)):
                return [Error(errstr_wrong % (letter, mo.group(1)))]

            # check 3: check if it's uppercase in "(_X)" form
            mo = re_lowercase_mnemonic.search(msgstr)
            if mo:
                return [Error(errstr_lowercase % mo.group(1))]
        return []
        
name = 'convention/accesskey'
description = '접근키를 올바로 번역했는지 검사합니다'
checker = AccessKeyCheck()
