# -*- coding: utf-8 -*-


class entry:
    def __init__(self):
        self.msgid = ''
        self.msgid_plural = ''
        self.msgstr = ''
        self.msgctxt = ''
        self.translator_comment = ''
        self.automatic_comment = ''
        self.references = []
        self.flags = set()

    # attributes handling
    def set_flag(self, flag):
        self.flags.add(flag)

    def unset_flag(self, flag):
        self.flags.remove(flag)

    def check_flag(self, flag):
        return flag in self.flags

    def is_fuzzy(self):
        return self.check_flag('fuzzy')

    def is_obsolete(self):
        return self.check_flag('obsolete')

    def is_untranslated(self):
        return (self.msgstr == '')

    def is_translated(self):
        return (not self.is_fuzzy() and
                not self.is_obsolete() and
                not self.is_untranslated())

    def is_no_wrap(self):
        return self.check_flag('no-wrap')

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
