# -*- coding: utf-8 -*-

import re
from KPC.classes import Error, BaseCheck

re_accesskey_gnome = re.compile(r'^[^_]*_([0-9A-Za-z])[^_]*$')
re_accesskey_kde = re.compile(r'^[^&]*&([0-9A-Za-z])[^_]*$')

re_accesskey = re.compile(r'^[^_]*[_&]([0-9A-Za-z])[^_]*$')

# GNOME 예외적인 경우:
# - 소문자로 시작하는 경우
# - "abc_DEF" 등 중간에 밑줄 다음에 대문자가 나오는 경우
re_accesskey_gnome_unlikely = re.compile(r'([a-z].*|.*[a-zA-Z]_[A-Z].*)')

# KDE 예외적인 경우:
# - 소문자로 시작하는 경우
# - XML entity처럼 보이는 경우
# - URL처럼 보이는 경우
re_accesskey_kde_unlikely = re.compile(r'([a-z]|.*&[a-zA-Z][a-zA-Z_-]*;|'
                                       '.*[a-z]://\S+/\S+&[0-9a-zA-Z].*=)')

errstr_no_accesskey = '번역문에 접근키가 없거나 두 개 이상입니다'
errstr_wrong = '\'%s\' vs \'%s\': 원문과 번역문의 접근키가 다릅니다'

re_lowercase_accesskey = re.compile('(\([_&][a-z]\))')
errstr_lowercase = '\"%s\": 접근키가 소문자입니다'


class AccessKeyCheck(BaseCheck):
    def check(self, entry, context):
        msgid = entry.msgid
        msgstr = entry.msgstr
        gnome_mo = re_accesskey_gnome.match(msgid)
        kde_mo = re_accesskey_kde.match(msgid)

        # doubts if the string really contains a access key
        if gnome_mo and re_accesskey_gnome_unlikely.match(msgid):
            gnome_mo = None
        if kde_mo and re_accesskey_kde_unlikely.match(msgid):
            kde_mo = None

        if gnome_mo or kde_mo:
            # too long string to be a label string
            if len(msgid) > 60:
                return []
            # GConf schema or GSettings schema file
            if entry.references and ('.schemas' in entry.references[0] or
                                     '.gschema' in entry.references[0]):
                return []

            if gnome_mo:
                letter = gnome_mo.group(1).upper()
            else:
                letter = kde_mo.group(1).upper()
            # check 1: if it's translated with the access key
            mo = re_accesskey.match(msgstr)
            if not mo:
                return [Error(errstr_no_accesskey)]

            # check 2: check if it's same
            if letter != mo.group(1).upper():
                return [Error(errstr_wrong % (letter, mo.group(1)))]

            # check 3: check if it's uppercase in "(_X)" form
            mo = re_lowercase_accesskey.search(msgstr)
            if mo:
                return [Error(errstr_lowercase % mo.group(1))]
        return []

name = 'convention/access-key'
description = '접근키를 올바로 번역했는지 검사합니다'
checker = AccessKeyCheck()
