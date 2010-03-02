# -*- coding: utf-8 -*-
# GNOME L10N administravia

import string
from KPC.classes import Error, HeaderCheck

class GnomeHeaderCheck(HeaderCheck):
    error = Error('새 번역팀 주소를 사용하십시오: <gnome-kr@googlegroups.com>')

    def check_fields(self, fields):
        if 'gnome-kr-hackers@lists.kldp.net' in fields['Language-Team']:
            return [self.error]

name = 'convention/gnome-team'

def check(entry):
    # FIXME: drop this legacy wrapper
    errors = GnomeHeaderCheck().check(entry)
    if errors:
        return (0, string.join([e.message for e in errors]))
    else:
        return (1, 0)

