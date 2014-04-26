# -*- coding: utf-8 -*-

# 바람직한 스타일이 아닌 번역 표현을 찾아낸다. 특히 각종 번역체.

import re
from KPC.classes import Error, BaseCheck

R = re.compile

PLURAL_JOSA_RE = '(도|로|만|에|은|을|이|의)'
# 많이 등장하는 명사만 쓴다
PLURAL_NOUN_RE = '(값|개발자|것|기능|기술|그림|글자|답변|디렉터리|메시지|' \
                 '문서|문자|분|사람|사진|설정|언어|점|질문|파일|팀|패키지|' \
                 '폴더|프로그램|플러그인|항목|활동)'
PLURAL_EXCEPT = '(' + '핸들' + PLURAL_JOSA_RE + ')'

SYLLABLE_WITH_T_RIEUL = '[%s]' % ''.join([chr(c) for c in
                                          range(0xAC00 + 8, 0xD7A4, 28)])
SYLLABLE_WITH_T_SSANGSIOS = '[%s]' % \
                            ''.join([chr(c) for c in
                                     range(0xAC00 + 0x14, 0xD7A4, 28)])

data = [
    # 임의의 복수형 표현을 찾아내기는 매우 힘들다. 다음 휴리스틱으로만 검사.
    # (0) (들)이라고 쓰여진 경우
    # (1) 일단 알려진 명사에 대한 복수형태를 찾고
    # (2) 들+조사 형태로 끝나는 경우를 찾는다
    {
        're': R('(' +
                '[\uac00-\ud7a3]+\(들\)' + '|' +
                PLURAL_NOUN_RE + '들' + '|' +
                '[\uac00-\ud7a3]+들' + PLURAL_JOSA_RE + '\s' + ')'),
        'error': '%s: 불필요한 복수형 표현',
        'except': R(PLURAL_EXCEPT),
    },

    # ...하기 위하여/위해 => ...하려면
    {
        're': R('[\uac00-\ud7a3]+기 위(하여|해)'),
        'error': '%s: 어색한 표현. "-하려면"과 같이 쓰십시오.',
    },

    # ...와 함께
    {
        're': R('\S+와 함께'),
        'error': '%s: 어색한 표현. 풀어서 써 보십시오.',
    },

    # ...에 의해
    {
        're': R('\S+에 의해'),
        'error': '%s: 어색한 표현. 수동태 문장을 바꿔 보십시오.',
    },

    # 필요로 하다
    {
        're': R('필요로 하\S+'),
        'error': '%s: 어색한 표현. "필요하다"와 같이 간결히 쓰십시오.',
    },

    # 필요가 있다
    {
        're': R('필요가 있\S+'),
        'error': '%s: 어색한 표현. "...해야 합니다"와 같이 간결히 쓰십시오.',
    },

    # ...할 것입니다
    {
        're': R('\S+' + SYLLABLE_WITH_T_RIEUL + ' 것입니다'),
        'error': '%s: 어색한 표현. "...합니다"와 같이 간결히 쓰십시오.',
        # 과거형인 "-했을 것입니다"는 예외
        'except': R('\S+' + SYLLABLE_WITH_T_SSANGSIOS + '을 것입니다'),
    },

    # ...하시기 바랍니다 것입니다
    {
        're': R('\S+시기 바랍니다'),
        'error': '%s: 어색한 표현. "...하십시오"와 같이 간결히 쓰십시오.',
    },

    # "N개의 아무개"
    {
        're': R('%\S*[du]개의 \S+'),
        'error': '%s: 어색한 표현. "몇개의 아무개" 대신 "아무개 몇개"와 같이 쓰십시오.',
    },

    # ...을 포함
    {
        're': R('\S+[를을이가] 포함\S+'),
        'error': '%s: 어색한 표현. "..이 들어 있다"와 같이 바꿔 쓰십시오.',
    },
]


class BadStyleCheck(BaseCheck):
    def check(self, entry, context):
        msgstr = entry.msgstr
        errors = []
        for entry in data:
            r = entry['re']
            errmsg = entry['error']
            mo = r.search(msgstr)
            if mo:
                if ('except' in entry) and entry['except'].match(mo.group(0)):
                    continue
                errors.append(Error(errmsg % mo.group(0)))
        return errors

name = 'language/badstyle'
description = '번역체 등 바람직하지 못한 스타일의 번역을 찾아냅니다'
checker = BadStyleCheck()
