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
    outstream.write(unicode(str,'utf-8'))

def error(str):
    errorstream.write(unicode(str,'utf-8'))

def outlines(lines):
    outstream.writelines(map(lambda s: unicode(s,'utf-8'), lines))

def errorlines(lines):
    errorstream.writelines(map(lambda s: unicode(s,'utf-8'), lines))

def eucstr(str):
    return unicode(str,'euc-kr').encode('utf-8')

if __name__ == '__main__':
    init()
    str = unicode('하하하하하', 'euc-kr').encode('utf-8')
    out(str)
