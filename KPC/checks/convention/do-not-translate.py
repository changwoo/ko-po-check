import re
from KPC.classes import Error, BaseCheck

R = re.compile
dnt_re = R('^translators.*: ?do not translate.* this text.*$')

class DoNotTranslateCheck(BaseCheck):
    errstr = '번역하지 말라는 표시가 되어 있는 원문을 번역했습니다'

    def check(self, entry, context):
        if len(entry.msgid) == 0 or entry.msgid == entry.msgstr:
            return []

        lines = entry.extracted_comment.split('\n')
        for line in lines:
            if dnt_re.match(line.lower()):
                return [Error(self.errstr)]
        else:
            return []

name = 'convention/do-not-translate'
description = '번역하지 말라고 표시된 원문을 번역한 경우를 찾아냅니다'
checker = DoNotTranslateCheck()
