# -*- coding: utf-8 -*-
'''Parse GNU gettext compliant PO (Portable Object) file.

'''

__all__ = ['parse_file', 'parse_entry', 'ParseError',
           'FUZZY', 'OBSOLETE', 'C_FORMAT', 'NO_C_FORMAT', 'NO_WRAP']

import po,re,string

ParseError = 'ParseError'

def c2rawstring(str):
    return eval('"'+str+'"')

FUZZY,OBSOLETE,C_FORMAT,NO_C_FORMAT,NO_WRAP = 1,2,4,8,16

def parse_file(file):
    reader = file
    lineno = 0
    catalog = po.catalog()
    try:
        (entry,lineno) = parse_entry(reader,lineno)
    except ParseError:
        raise ParseError, lineno
    catalog.add_entry(entry)
    content_type = catalog.metadata['Content-Type']
    charset = re.compile('charset=(.+)$').search(content_type).group(1)
    while 1:
        try:
            (entry,lineno) = parse_entry(reader,lineno)
        except ParseError, l:
            raise ParseError, l
        if not entry:
            return catalog
        try:
            entry.translator_comment = unicode(entry.translator_comment,charset)
            entry.msgstr = unicode(entry.msgstr,charset)
            entry.msgid = unicode(entry.msgid,charset)
        except:
            raise ParseError, lineno
        catalog.add_entry(entry)

STATE_FIRST,STATE_COMMENT,STATE_ECOMMENT,STATE_MSGCTXT,STATE_MSGID,STATE_MSGSTR = 1,2,3,4,5,6
emptyline_re = re.compile(r'^\s*$')
translator_comment_re = re.compile(r'^\#( (.*))?$')
automatic_comment_re = re.compile(r'^\#. (.*)$')
reference_re = re.compile(r'^\#: (.*)$')
flag_re = re.compile(r'^\#, (.*)$')
string_re = re.compile(r'^\"(.*)\"\w*')

def read_string(fmt):
    try:
        str = string_re.match(fmt).group(1)
    except:
        raise ParseError
    return c2rawstring(str)

import codecs

def parse_entry(file,lineno):
    state = STATE_FIRST
    new_entry = po.entry()
    while 1:
        lineno += 1
        line = file.readline()
        if not line:                    # EOF
            if state == STATE_FIRST or state == STATE_COMMENT:
                return (None,lineno)    # no more messages -- return nothing
            elif state != STATE_MSGSTR:
                raise ParseError, lineno        # unexpected EOF
            else:
                return (new_entry,lineno)
        if emptyline_re.match(line):
            if state == STATE_FIRST or state == STATE_COMMENT:
                continue
            elif state != STATE_MSGSTR:
                raise ParseError, lineno
            else:
                return (new_entry,lineno)
        if line[-1] == '\n':            # remove the trailing newline
            line = line[:-1]
        if line[:3] == '#~ ':
            new_entry.set_flag(OBSOLETE)
            line = line[3:]
        # comments
        if line[0] == '#':
            if state == STATE_FIRST:
                state = STATE_COMMENT
            if len(line) == 1:
                new_entry.translator_comment += '\n'
            elif line[1] == ' ':          # automatic comment
                new_entry.translator_comment += line[2:] + '\n'
            elif line[1] == ':':
                state = STATE_ECOMMENT
                new_entry.references += string.split(line[3:],' ')
            elif line[1] == ',':
                state = STATE_ECOMMENT
                for flag in string.split(line[3:], ', '):
                    if flag == 'c-format':
                        new_entry.set_flag(C_FORMAT)
                    elif flag == 'no-c-format':
                        new_entry.set_flag(NO_C_FORMAT)
                    elif flag == 'fuzzy':
                        new_entry.set_flag(FUZZY)
                    elif flag == 'no-wrap':
                        new_entry.set_flag(NO_WRAP)
                pass
            elif line[1] == '~':
                state = STATE_ECOMMENT
                pass
        else:
            if line[:9] == 'msgctxt "':
                state = STATE_MSGCTXT
                try:
                    new_entry.msgctxt += read_string(line[8:])
                except ParseError:
                    raise ParseError, lineno
            elif line[:7] == 'msgid "':
                state = STATE_MSGID
                try:
                    new_entry.msgid += read_string(line[6:])
                except ParseError:
                    raise ParseError, lineno
                new_entry.msgid_lineno = lineno
            elif line[:14] == 'msgid_plural "':
                state = STATE_MSGID
                new_entry.msgid_plural += read_string(line[13:])
            elif line[:8] == 'msgstr "':
                state = STATE_MSGSTR
                new_entry.msgstr += read_string(line[7:])
                new_entry.msgstr_lineno = lineno
            elif line[:7] == 'msgstr[':
                state = STATE_MSGSTR
                new_entry.msgstr += read_string(line[10:])
                new_entry.msgstr_lineno = lineno
            elif line[0] == '"':
                if state == STATE_MSGID:
                    new_entry.msgid += read_string(line)
                elif state == STATE_MSGSTR:
                    new_entry.msgstr += read_string(line)
                elif state == STATE_MSGCTXT:
                    new_entry.msgctxt += read_string(line)
                else:
                    raise ParseError, lineno
            else:
                raise ParseError, lineno
            
    #new_entry.msgid += line
    return (new_entry,lineno)
        
        
def test():
    import sys
    if sys.argv[1:]:
        fn = sys.argv[1]
        if fn == '-':
            fp = sys.stdin
        else:
            fp = open(fn)
    else:
        import StringIO
        fp = StringIO.StringIO(test_input)
    catalog = parse_file(fp)
    print str(catalog)

if __name__ == '__main__':
    test()
