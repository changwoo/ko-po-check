# -*- coding: utf-8 -*-
# terminology/common-labels

# 전형적인 번역문을 일관적으로 유지

import string, re
from KPC.classes import Error, BaseCheck

R = re.compile
def R(re_msgid, re_msgstr, label_msgid, label_msgstr):
    return (re.compile(re_msgid), re.compile(re_msgstr),
            label_msgid, label_msgstr)

data = [R('^View .*', '^.* 보기', 'View ...', '... 보기'),
        R('^Show .*', '^.* (보이기|표시)', 'Show ...', '... 보이기(표시)'),
        R('^Hide .*', '^.* 숨기기', 'Hide ...', '... 숨기기'),
       ]

def normalize_msg(msg):
    try:
        if msg[-3:] == '...':
            msg = msg[:-3]
        if msg[-4:-2] == '(_' and msg[-1:] == ')':
            msg = msg[:-4]
    except:
        pass
    msg = msg.replace('_', '')
    return msg

class CommonLabelsCheck(BaseCheck):
    errstr = '%s: \"%s\" 형태는 \"%s\" 형태와 같이 번역합니다'

    # 레이블이면 True
    def identify(self, entry):
        # 여러 줄 레이블 아님
        if '\n' in entry.msgid:
            return False
        # GConf schema or GSettings schema file
        if entry.references and ('.schemas' in entry.references[0] or
                                 '.gschema' in entry.references[0]):
            return False

        words = [x for x in entry.msgid.split(' ') if len(x)]
        # 모든 단어가 대문자로 시작하면 레이블
        if ''.join([x[0] for x in words]).isupper():
            return True
        # 단축키가 있으면 
        if '_' in entry.msgid:
            return True
        try:
            if entry.msgid[-3:] == '...':
                return True
        except:
            pass
        return False

    def check(self, entry):
        if not self.identify(entry):
            return []
        msgid = normalize_msg(entry.msgid)
        msgstr = normalize_msg(entry.msgstr)
        for (re_msgid, re_msgstr, label_msgid, label_msgstr) in data:
            if re_msgid.match(msgid):
                if not re_msgstr.match(msgstr):
                    return [Error(self.errstr %
                                  (entry.msgstr, label_msgid, label_msgstr))]
                else:
                    break
        return []

name = 'terminology/common-labels'
description = '전형적인 형태의 레이블을 일관적으로 번역했는지 검사합니다'
checker = CommonLabelsCheck()
