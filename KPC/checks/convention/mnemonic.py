# -*- coding: utf-8 -*-

import re, string

name = 'convention/mnemonic'
description = "접근키를 올바로 번역했는지 검사합니다"

re_mnemonic = re.compile('^[^_]*[_&]([0-9A-Za-z])[^_]*$')
group_mnemonic = 1

# 예외적인 경우:
# "abc_DEF" 등 중간에 밑줄 다음에 대문자가 나오는 경우
# "translator_credits" GNOME magic
# &amp; intltool에서 XML에서 변환하면서 unescape되지 않은 몇몇 케이스
re_mnemonic_unlikely = re.compile('(^[^_]*[a-zA-Z]_[A-Z][^_]*$|^translator_credits.*|.*%[ds].*|.*&amp;)')

error_string_no_mnemonic = u'번역문에 접근키가 없거나 두 개 이상입니다'
error_string_wrong = u'\'%s\' vs \'%s\': 원문과 번역문의 접근키가 다릅니다'

re_lowercase_mnemonic = re.compile('(\([_&][a-z]\))')
error_string_lowercase = u'\"%s\": 접근키가 소문자입니다'

def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    mo = re_mnemonic.match(msgid)
    if mo:
        # doubts if the string really contains a mnemonic
        if re_mnemonic_unlikely.match(msgid):
            return (1, '')
        if len(msgid) > 60:
            # too long string to be a label string
            return (1, '')
        if entry.references and entry.references[0].find('.schemas') >= 0:
            # GNOME schema file
            return (1, '')
        
        letter = string.upper(mo.group(group_mnemonic))
        # check 1: if it's translated with the mnemonic
        mo = re_mnemonic.match(msgstr)
        if not mo:
            return (0, error_string_no_mnemonic)

        # check 2: check if it's same
        if letter != string.upper(mo.group(group_mnemonic)):
            return (0, error_string_wrong % (letter, mo.group(group_mnemonic)))

        # check 3: check if it's uppercase in "(_X)" form
        mo = re_lowercase_mnemonic.search(msgstr)
        if mo:
            return (0, error_string_lowercase % mo.group(1))
    return (1, '')    

if __name__ == '__main__':
    import sys
    class entry:
        pass
    entry.msgid = sys.stdin.readline()
    entry.msgstr = sys.stdin.readline()
    entry.references = []
    t,e = check(entry)
    if not t:
        print e
    else:
        print 'Success'
