import re, string

name = "copyright"

copyright_re = re.compile(r"^([Cc]opyright )?\([Cc]\) ")

import localeutil
e = localeutil.eucstr

error_string = e("copyright notice�� �����ϸ� �� �˴ϴ�")

def check(msgid,msgstr):
    msgid_lines = string.split(msgid,"\n")
    msgstr_lines = string.split(msgstr,"\n")
    lineno = 0
    for line in msgid_lines:
        if copyright_re.match(line) and lineno < len(msgstr_lines) and line != msgstr_lines[lineno]:
            return (0,error_string)
        lineno+=1
    return (1,"")

if __name__ == '__main__':
    import sys
    msgid = sys.stdin.readline()
    msgstr = sys.stdin.readline()
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print "Success"
