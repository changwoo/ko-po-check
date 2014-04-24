class Error:
    '''An individual error from a check against an entry. One check
    usually returns list of errors or empty list if there's no error.
    '''
    SUCCESS = 0
    DEPRECATED = 1
    WARNING = 2
    ERROR = 3

    def __init__(self, message):
        self.pos = 0
        self.level = Error.ERROR
        self.message = message


class BaseCheck:
    '''Base class to check an entry from PO files. Subclasses should
    implement check() function. check() returns list of errors if any.
    '''
    def check(self, entry):
        return []


class CheckList(BaseCheck):
    '''Container class to hold other check classes. check() returns
    all errors from the contained sub-checks.
    '''
    def __init__(self, l=[]):
        self.checks = l

    def add(self, check):
        self.checks.append(check)

    def check(self, entry):
        ret = []
        for c in self.checks:
            ret += c.check(self, entry)
        return ret


class HeaderCheck(BaseCheck):
    '''Base class to check the header entries. Subclasses should
    implement check_header() function.
    '''
    def check(self, entry):
        # header messages only
        if entry.msgid != '':
            return []
        fields = {}
        # parse msgstr
        for line in entry.msgstr.split('\n'):
            try:
                k, v = line.split(': ', 1)
                fields[k] = v
            except ValueError:
                pass
        return self.check_header(entry, fields)
