# -*- coding: utf-8 -*-
# terminology/common-labels

# 전형적인 번역문을 일관적으로 유지

import re
from KPC.classes import Error, BaseCheck

data = [
    {
        're_msgid': re.compile('^View .*'),
        're_msgstr': re.compile('^.* 보기'),
        'label_msgid': 'View ...',
        'label_msgstr': '... 보기',
        're_exception': re.compile('^View only$')
    },
    {
        're_msgid': re.compile('^Show .*'),
        're_msgstr': re.compile('^.* (보이기|표시)'),
        'label_msgid': 'Show ...',
        'label_msgstr': '... 보이기(표시)',
        're_exception': None
    },
    {
        're_msgid': re.compile('^Hide .*'),
        're_msgstr': re.compile('^.* 숨기기'),
        'label_msgid': 'Hide ...',
        'label_msgstr': '... 숨기기',
        're_exception': None
    },
]


def normalize_msg(msg):
    try:
        if msg.endswith('...'):
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

    def check(self, entry, context):
        if not self.identify(entry):
            return []
        msgid = normalize_msg(entry.msgid)
        msgstr = normalize_msg(entry.msgstr)
        for d in data:
            re_msgid = d['re_msgid']
            re_msgstr = d['re_msgstr']
            label_msgid = d['label_msgid']
            label_msgstr = d['label_msgstr']
            re_except = d['re_exception']

            if re_msgid.match(msgid):
                if re_msgstr.match(msgstr):
                    break
                if re_except and re_except.match(msgid):
                    break
                return [Error(self.errstr %
                              (entry.msgstr, label_msgid, label_msgstr))]
        return []

name = 'terminology/common-labels'
description = '전형적인 형태의 레이블을 일관적으로 번역했는지 검사합니다'
checker = CommonLabelsCheck()
