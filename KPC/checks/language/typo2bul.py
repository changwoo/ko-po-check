# -*- coding: utf-8 -*-

import string,re

name = 'language/typo2bul'
description = '두벌식 키보드를 사용할 때 발생할 수 있는 오타를 찾아냅니다'

typo = '('+string.join([
    '밍나합니다',
    '거싱',
    '살마',
    '[가-힝]빈다'
    ], '|')+')'

typo_re = re.compile(typo.decode('utf-8'))
typo_error = u'\"%s\": 두벌식 오타로 보입니다'

def check(msgid,msgstr):
    ret = 1
    errmsg = ''
    str = msgstr
    while 1:
        mo = typo_re.search(str)
        if mo:
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
    msgid = unicode(sys.stdin.readline(),'euckr')
    msgstr = unicode(sys.stdin.readline(),'euckr')
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print 'Success'

# Local Variables:
# coding: utf-8
# End:
