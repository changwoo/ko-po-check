# -*- coding: utf-8 -*-

# 그놈 프로그램에서 많이 쓰는 libegg에서 복사한 코드에 들어 있는 메시지
# 통일

from KPC.classes import Error, BaseCheck

data = [
    {'ref': 'eggdesktopfile.c',
     'msgid': 'File is not a valid .desktop file',
     'msgstr': '올바른 .desktop 파일이 아닙니다'},

    {'ref': 'eggdesktopfile.c',
     'msgid': 'Unrecognized desktop file Version \'%s\'',
     'msgstr': 'desktop 파일 버전을 (\'%s\') 인식할 수 없습니다'},

    {'ref': 'eggdesktopfile.c',
     'msgid': 'Starting %s',
     'msgstr': '%s 시작'},

    {'ref': 'eggdesktopfile.c',
     'msgid': 'Application does not accept documents on command line',
     'msgstr': '명령행에서 문서를 지정할 수 없는 프로그램입니다'},

    {'ref': 'eggdesktopfile.c',
     'msgid': 'Unrecognized launch option: %d',
     'msgstr': '알 수 없는 실행 옵션: %d'},

    {'ref': 'eggdesktopfile.c',
     'msgid': 'Can\'t pass document URIs to a \'Type=Link\' desktop entry',
     'msgstr': '문서 URI는 \'Type=Link\' desktop 항목에 넘길 수 없습니다'},

    {'ref': 'eggdesktopfile.c',
     'msgid': 'Not a launchable item',
     'msgstr': '실행할 수 있는 항목이 없습니다'},

    {'ref': 'eggsmclient.c',
     'msgid': 'Disable connection to session manager',
     'msgstr': '세션 관리자에 연결하지 않습니다'},

    {'ref': 'eggsmclient.c',
     'msgid': 'Specify file containing saved configuration',
     'msgstr': '설정을 저장할 파일을 지정합니다'},

    {'ref': 'eggsmclient.c',
     'msgid': 'FILE',
     'msgstr': '<파일>'},

    {'ref': 'eggsmclient.c',
     'msgid': 'Specify session management ID',
     'msgstr': '세션 관리 ID를 지정합니다'},

    {'ref': 'eggsmclient.c',
     'msgid': 'ID',
     'msgstr': '<ID>'},

    {'ref': 'eggsmclient.c',
     'msgid': 'Session management options:',
     'msgstr': '세션 관리 옵션:'},

    {'ref': 'eggsmclient.c',
     'msgid': 'Show session management options',
     'msgstr': '세션 관리 옵션을 표시합니다'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': 'Show “_%s”',
     'msgstr': '“_%s” 보이기'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': '_Move on Toolbar',
     'msgstr': '도구 모음에서 옮기기(_M)'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': 'Move the selected item on the toolbar',
     'msgstr': '도구 모음에서 선택한 항목을 옮깁니다'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': '_Remove from Toolbar',
     'msgstr': '도구 모음에서 제거(_R)'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': 'Remove the selected item from the toolbar',
     'msgstr': '도구 모음에서 선택한 항목을 제거합니다'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': '_Delete Toolbar',
     'msgstr': '도구 모음 삭제(_D)'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': 'Remove the selected toolbar',
     'msgstr': '선택한 도구 모음을 제거합니다'},

    {'ref': 'egg-editable-toolbar.c',
     'msgid': 'Separator',
     'msgstr': '구분선'},
]


class LibeggCheck(BaseCheck):
    errstr = '일관성을 위해 다음과 같이 번역합니다: %s'

    def check(self, entry, context):
        for d in data:
            if [x for x in entry.references if (d['ref']+':') in x]:
                if entry.msgid == d['msgid'] and entry.msgstr != d['msgstr']:
                    return [Error(self.errstr % d['msgstr'])]
        return []

name = 'terminology/libegg'
description = 'libegg에서 가져온 코드의 번역이 통일된 번역인지 검사합니다'
checker = LibeggCheck()
