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
    def _get_context(self, entry):
        if not hasattr(self, 'get_context'):
            return {}
        fields = {}
        # parse msgstr
        for line in entry.msgstr.split('\n'):
            try:
                k, v = line.split(': ', 1)
                fields[k] = v
            except ValueError:
                pass
        return self.get_context(entry, fields)

    def _check(self, entry, context):
        return self.check(entry, context)


class HeaderCheck(BaseCheck):
    '''Base class to check the header entries. Subclasses should
    implement check_header() function.
    '''
    def check(self, entry, context):
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


class CheckList(BaseCheck):
    '''Container class to perform all child checks
    '''
    def __init__(self, children=[]):
        self.children = children.copy()

    def check(self, entry, context):
        r = []
        for c in self.children:
            k = c.check(entry, context)
            if k:
                r += k
        return r
