# -*- coding: utf-8 -*-

import re, string

name = "mnemonic"

e = lambda s: unicode(s,'utf-8')

re_mnemonic = re.compile("^[^_]*_([0-9A-Za-z])[^_]*$")
re_mnemonic_unlikely = re.compile("(^[^_]*[a-zA-Z]_[A-Z][^_]*$|^translator_credits.*|.*%[ds].*)")
group_mnemonic = 1
error_string_no_mnemonic = e("번역문에 mnemonic이 없거나 두 개 이상입니다")
error_string_wrong = e("\'%s\' vs \'%s\': 원문과 번역문의 mnemonic이 다릅니다")

re_lowercase_mnemonic = re.compile("(\([_&][a-z]\))")
error_string_lowercase = e("\"%s\": mnemonic이 소문자입니다")

def check(msgid,msgstr):
    mo = re_mnemonic.match(msgid)
    if mo:
        # doubts if the string really contains a mnemonic
        if re_mnemonic_unlikely.match(msgid):
            return (1, "")
        if len(msgid) > 60:                   # too long to be a label string
            return (1, "")
        
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
    return (1, "")    

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
