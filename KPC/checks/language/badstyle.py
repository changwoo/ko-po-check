# -*- coding: utf-8 -*-

# 바람직한 스타일이 아닌 번역 표현을 찾아낸다. 특히 각종 번역체.

import string,re
from KPC.classes import Error, BaseCheck

R = re.compile

PLURAL_JOSA_RE = '(도|로|만|에|은|을|이|의)'
# 많이 등장하는 명사만 쓴다
PLURAL_NOUN_RE = '(값|개발자|것|기능|기술|그림|글자|답변|디렉터리|메시지|문서|문자|분|사람|사진|설정|언어|점|질문|파일|팀|패키지|폴더|프로그램|플러그인|항목|활동)'
PLURAL_EXCEPT = '(' + '핸들' + PLURAL_JOSA_RE + ')'

data = [
    # 임의의 복수형 표현을 찾아내기는 매우 힘들다. 다음 휴리스틱으로만 검사.
    # (0) (들)이라고 쓰여진 경우
    # (1) 일단 알려진 명사에 대한 복수형태를 찾고
    # (2) 들+조사 형태로 끝나는 경우를 찾는다
    { 're': R('(' +
              '[\uac00-\ud7a3]+\(들\)' + '|' +
              PLURAL_NOUN_RE + '들' + '|' +
              '[\uac00-\ud7a3]+들' + PLURAL_JOSA_RE + '\s' + ')'),
      'error': '%s: 불필요한 복수형 표현',
      'except': R(PLURAL_EXCEPT),
      },
]

class BadStyleCheck(BaseCheck):
    def check(self, entry):
        msgid = entry.msgid
        msgstr = entry.msgstr
        errors = []
        for entry in data:
            r = entry['re']
            errmsg = entry['error']
            e = entry['except']

            mo = r.search(msgstr)
            if mo and not e.match(mo.group(0)):
                errors.append(Error(errmsg % mo.group(0)))
        return errors

name = 'language/badstyle'
description = '번역체 등 바람직하지 못한 스타일의 번역을 찾아냅니다'
checker = BadStyleCheck()
