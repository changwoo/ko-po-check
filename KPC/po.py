# -*- coding: utf-8 -*-

FUZZY = 1
OBSOLETE = 2
C_FORMAT = 4
NO_C_FORMAT = 8
PYTHON_FORMAT = 16
NO_WRAP = 32


class entry:
    def __init__(self):
        self.msgid = ''
        self.msgid_plural = ''
        self.msgstr = ''
        self.msgctxt = ''
        self.translator_comment = ''
        self.automatic_comment = ''
        self.references = []
        self.flag = 0

    # attributes handling
    def set_flag(self, flag):
        self.flag = self.flag | flag

    def unset_flag(self, flag):
        self.flag = self.flag & ~flag

    def is_fuzzy(self):
        return (self.flag & FUZZY)

    def is_obsolete(self):
        return (self.flag & OBSOLETE)

    def is_untranslated(self):
        return (self.msgstr == '')

    def is_translated(self):
        return (not self.is_fuzzy() and
                not self.is_obsolete() and
                not self.is_untranslated())

    def is_c_format(self):
        return (self.flag & C_FORMAT)

    def is_no_c_format(self):
        return (self.flag & NO_C_FORMAT)

    def is_python_format(self):
        return (self.flag & PYTHON_FORMAT)

    def is_no_wrap(self):
        return (self.flag & NO_WRAP)

    def __repr__(self):
        return repr(self.msgid) + ':::' + repr(self.msgstr)


class catalog:
    def __init__(self):
        self.entries = []
        self.metadata = {}
        self.textdomain = ''
        self.language = 'ko'

    def add_entry(self, entry):
        if (entry.msgid == ''):         # header entry
            a = entry.msgstr.split('\n')
            for l in a:
                if len(l) == 0:
                    continue
                k, v = l.split(': ', 1)
                self.metadata[k] = v
        self.entries.append(entry)

    def settextdomain(self, d):
        self.textdomain = d
