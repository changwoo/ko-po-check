import re, string

name = "copyright"

copyright_re = re.compile(r"^([Cc]opyright )?\([Cc]\) ")

def euc(s):
    return unicode(s,'euc-kr').encode('utf-8')

error_string = euc("copyright notice는 번역하면 안 됩니다")

def check(msgid,msgstr):
    msgid_lines = string.split(msgid,"\n")
    msgstr_lines = string.split(msgstr,"\n")
    lineno = 0
    for line in msgid_lines:
        if copyright_re.match(line) and line != msgstr_lines[lineno]:
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
