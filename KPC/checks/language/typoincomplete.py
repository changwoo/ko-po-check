# -*- coding: utf-8 -*-

import string,re

name = "language/typoincomplete"
description = "오타로 보이는 불완전한 음절을 찾아냅니다"

typo_re = re.compile(u'([\u3131-\u318E]+)')
typo_exception_re = re.compile(u'^[\u3131-\u318E]-[\u3131-\u318E]') # gdm
typo_error = u'\"%s\": 음절이 불완전합니다.  오타로 보입니다'

def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    ret = 1
    errmsg = ''
    str = msgstr
    while 1:
        mo = typo_re.search(str)
        if mo and not typo_exception_re.match(str):
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += typo_error % mo.group(1)
            str = str[mo.end():]
        else:
            break;
    return (ret, errmsg)

if __name__ == '__main__':
    import sys
    class entry:
        pass
    entry.msgid = sys.stdin.readline()
    entry.msgstr = sys.stdin.readline()
    t,e = check(entry)
    if not t:
        print e
    else:
        print 'Success'
