# -*- coding: utf-8 -*-
# GNOME L10N administravia

from KPC.classes import Error, HeaderCheck, CheckList

class TeamMailCheck(HeaderCheck):
    new_addr = '<gnome-kr@googlegroups.com>'
    old_addr = '<gnome-kr-hackers@lists.kldp.net>'
    error = Error('새 번역팀 주소를 사용하십시오: %s' % new_addr)

    def check_header(self, entry, fields):
        try:
            value = fields['Language-Team']
            if self.old_addr in value:
                return [self.error]
            if value.startswith('GNOME Korea') and not self.new_addr in value:
                return [self.error]
        except KeyError:
            pass
        return []


name = 'convention/gnome-team'
description = '그놈 한국어 번역팀 관련 사항을 검사합니다'
checker = CheckList([TeamMailCheck()])

