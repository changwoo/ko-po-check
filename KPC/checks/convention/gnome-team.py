# -*- coding: utf-8 -*-
# GNOME L10N administravia

import string
from KPC.classes import Error, HeaderCheck

class GnomeHeaderCheck(HeaderCheck):
    error = Error('새 번역팀 주소를 사용하십시오: <gnome-kr@googlegroups.com>')

    def check_fields(self, fields):
        try:
            if 'gnome-kr-hackers@lists.kldp.net' in fields['Language-Team']:
                return [self.error]
        except KeyError:
            pass
        return []

name = 'convention/gnome-team'
description = '그놈 한국어 번역팀 관련 사항을 검사합니다'
checker = GnomeHeaderCheck()
