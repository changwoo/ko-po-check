import locale
import codecs, sys

__all__ = ["init", "out", "error"]

outstream = sys.stdout
errorstream = sys.stderr

def init():
    localename = locale.setlocale(locale.LC_CTYPE, "")
    try:
        charset = locale.nl_langinfo(locale.CODESET)
    except AttributeError:
        import re
        mo = re.compile("\.([^\.@]+)(@[^@]+)?").search(localename)
        if (mo):
            charset = mo.group(1)
        else:
            # fallback - euc-kr 사용
            charset = 'euc-kr'
    streamwriter = codecs.lookup(charset)[3]
    global outstream, errorstream
    outstream = streamwriter(sys.stdout)
    errorstream = streamwriter(sys.stderr)

def out(str):
    outstream.write(str)

def error(str):
    errorstream.write(str)

def outlines(lines):
    outstream.writelines(lines)

def errorlines(lines):
    errorstream.writelines(lines)

def eucstr(str):
    return unicode(str,'euc-kr')

if __name__ == '__main__':
    init()
    str = unicode('하하하하하', 'euc-kr').encode('utf-8')
    out(str)
