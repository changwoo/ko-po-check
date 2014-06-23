# -*- coding: utf-8 -*-
# header checks

from KPC.classes import Error, HeaderCheck


class CommonHeaderCheck(HeaderCheck):
    def check_header(self, entry, fields):
        result = []
        # Report-Msgid-Bugs-To: 내용이 없는 경우
        try:
            if fields['Report-Msgid-Bugs-To'] == '':
                errmsg = 'Report-Msgid-Bugs-To: 비어 있습니다. ' \
                         '버그 보고하는 메일 혹은 웹 주소를 쓰십시오'
                result.append(Error(errmsg))
        except KeyError:
            pass
        # 
        if fields['Last-Translator'].startswith('FULL NAME'):
            errmsg = 'Last-Translator: 기본값을 바꾸지 않았습니다. 번역자 이름을 쓰십시오'
            result.append(Error(errmsg))
        if 'EMAIL@ADDRESS' in fields['Last-Translator']:
            errmsg = 'Last-Translator: 기본값을 바꾸지 않았습니다. 번역자 메일 주소를 쓰십시오'
            result.append(Error(errmsg))
        # Language-Team: 쓰지 않았거나 gettext 기본값을 바꾸지 않은 경우
        if 'Language-Team' not in fields:
            errmsg = 'Language-Team: 필드가 없습니다. 번역 팀이 따로 없으면 본인 주소를 쓰십시오'
            result.append(Error(errmsg))
        elif fields['Language-Team'] == '':
            errmsg = 'Language-Team: 비어 있습니다. 번역 팀이 따로 없으면 본인 주소를 쓰십시오'
            result.append(Error(errmsg))
        elif 'ko@li.org' in fields['Language-Team']:
            errmsg = 'Language-Team: 기본값을 바꾸지 않았습니다. 해당 번역팀 메일 주소를 쓰십시오'
            result.append(Error(errmsg))
        # Content-Type: UTF-8 추천
        if not 'charset=utf-8' in fields['Content-Type'].lower():
            errmsg = 'Content-Type: UTF-8 사용을 추천합니다 (charset=UTF-8)'
            result.append(Error(errmsg))
        # Plural-Forms: 한국어에 대한 복수형이 아닌 경우
        correct_value = 'nplurals=1; plural=0;'
        try:
            if fields['Plural-Forms'] != correct_value:
                errmsg = 'Plural-Forms: 한국어는 다음과 같이 씁니다: "%s"'
                result.append(Error(errmsg % correct_value))
        except KeyError:
            pass
        return result

name = 'convention/common-header'
description = '헤더 메시지가 올바른지 검사합니다'
checker = CommonHeaderCheck()
