# -*- coding: utf-8 -*-
# Docbook XML markup check

name = 'convention/markup-docbook'
description = "DocBook 마크업의 짝이 맞는지 검사합니다"

from xml.parsers.expat import ParserCreate
from xml.parsers.expat import ExpatError

# 메세지에 대해 XML 파서를 돌려 well formed인지 검사하고, 태그가 알려진
# DocBook 태그인지 검사한다.
# FIXME: comment에서 XML 파일인지 여부를 받아서 XML이 아니면 검사를 하지 않는다.

known_db_tags = set(['acronym', 'anchor', 'application', 'citerefentry', 'citetitle', 'classname', 'command', 'computeroutput', 'email', 'emphasis', 'entry', 'envar', 'filename', 'firstterm', 'footnote', 'glossterm', 'guibutton', 'guiicon', 'guilabel', 'guimenu', 'guimenuitem', 'guisubmenu', 'indexterm', 'informalexample', 'informaltable', 'interface', 'itemizedlist', 'keycap', 'keycombo', 'keysym', 'link', 'listitem', 'literal', 'manvolnum', 'menuchoice', 'option', 'orderedlist', 'para', 'phrase', 'primary', 'prompt', 'quote', 'refentrytitle', 'remark', 'replaceable', 'row', 'screen', 'screen', 'secondary', 'see', 'sgmltag', 'shortcut', 'systemitem', 'tbody', 'term', 'tertiary', 'tgroup', 'thead', 'title', 'trademark', 'ulink', 'uri', 'userinput', 'variablelist', 'varlistentry', 'varname', 'xref'])

tag_error_string = u'XML 태그의 짝이 맞지 않습니다'
notdb_error_string = u'<%s>: 알려진 DocBook 태그가 아닙니다'

class NotDocBook(Exception):
    pass

def check_db_tags(name):
    if name == 'DummyTag':
        pass
    elif name[:12] == 'placeholder-':
        # gnome-doc-utils magic
        pass
    elif not name in known_db_tags:
        raise NotDocBook, name

def start_element(name,attr):
    check_db_tags(name)

def end_element(name):
    check_db_tags(name)

def check(msgid,msgstr):
    if msgid == 'translator-credits': # gnome-doc-utils magic
        return (1,'')
    parser = ParserCreate()
    parser.StartElementHandler = start_element
    parser.EndElementHandler = end_element
    parser.UseForeignDTD(True)
    try:
        parser.Parse('<DummyTag>' + msgstr + '</DummyTag>')
    except ExpatError, e:
        return (0, tag_error_string)
    except NotDocBook, e:
        return (0, notdb_error_string % e)
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
