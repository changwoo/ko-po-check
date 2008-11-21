# -*- coding: utf-8 -*-
import re, string

name = "convention/copyright"
description = "저작권 표시에 대한 번역문을 검사합니다"

copyright_re = re.compile(r"^([Cc]opyright )?\([Cc]\) ")

error_string = u'copyright notice는 번역하면 안 됩니다'

def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    msgid_lines = string.split(msgid,"\n")
    msgstr_lines = string.split(msgstr,"\n")
    lineno = 0
    for line in msgid_lines:
        if copyright_re.match(line) and lineno < len(msgstr_lines) and line != msgstr_lines[lineno]:
            return (0,error_string)
        lineno+=1
    return (1,'')

if __name__ == '__main__':
    import sys
    msgid = sys.stdin.readline()
    msgstr = sys.stdin.readline()
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print 'Success'
