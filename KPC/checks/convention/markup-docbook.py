# -*- coding: utf-8 -*-
# Docbook XML markup check

from xml.parsers.expat import ParserCreate
from xml.parsers.expat import ExpatError
from KPC.classes import Error, BaseCheck

# 메시지에 대해 XML 파서를 돌려 well formed인지 검사하고, 태그가 알려진
# DocBook 태그인지 검사한다.

# DocBook XML의 태그는 수백 가지에 달하지만, 결벽증 마냥 모든 걸 나열할
# 필요는 없고 실제 발견될 때마다 추가하도록 한다.

known_db_tags = set([
    'acronym',
    'address',
    'anchor',
    'application',
    'citerefentry',
    'citetitle',
    'city',
    'classname',
    'command',
    'computeroutput',
    'country',
    'email',
    'emphasis',
    'entry',
    'envar',
    'filename',
    'firstterm',
    'footnote',
    'footnoteref',
    'glossterm',
    'guibutton',
    'guiicon',
    'guilabel',
    'guimenu',
    'guimenuitem',
    'guisubmenu',
    'indexterm',
    'informalexample',
    'informaltable',
    'interface',
    'interfacename',
    'itemizedlist',
    'keycap',
    'keycombo',
    'keysym',
    'link',
    'listitem',
    'literal',
    'manvolnum',
    'menuchoice',
    'option',
    'orderedlist',
    'para',
    'phrase',
    'postcode',
    'primary',
    'prompt',
    'quote',
    'refentrytitle',
    'remark',
    'replaceable',
    'row',
    'screen',
    'screen',
    'secondary',
    'see',
    'sgmltag',
    'shortcut',
    'state',
    'street',
    'subscript',
    'superscript',
    'systemitem',
    'tbody',
    'term',
    'tertiary',
    'tgroup',
    'thead',
    'title',
    'trademark',
    'ulink',
    'uri',
    'userinput',
    'variablelist',
    'varlistentry',
    'varname',
    'xref'
])

tag_error_string = 'XML 태그의 짝이 맞지 않습니다'
notdb_error_string = '<%s>: 알려진 DocBook 태그가 아닙니다'


class NotDocBook(Exception):
    pass


def check_db_tags(name):
    if name == 'KPC_DummyTag':
        pass
    elif name[:12] == 'placeholder-':
        # old gnome-doc-utils magic
        pass
    elif name[:7] == '_:item-' or name[:7] == '_:link-':
        # newer gnome-doc-utils magic
        pass
    elif not name in known_db_tags:
        raise NotDocBook(name)


def start_element(name, attr):
    check_db_tags(name)


def end_element(name):
    check_db_tags(name)


class MarkupDocbookCheck(BaseCheck):
    def check(self, entry, context):
        if not entry.references or not '.xml:' in entry.references[0]:
            # not from an XML file
            return []
        msgid = entry.msgid
        msgstr = entry.msgstr
        if msgid == 'translator-credits':  # gnome-doc-utils magic
            return []
        parser = ParserCreate()
        parser.StartElementHandler = start_element
        parser.EndElementHandler = end_element
        parser.UseForeignDTD(True)
        try:
            parser.Parse('<KPC_DummyTag>' + msgstr + '</KPC_DummyTag>')
        except ExpatError as e:
            return [Error(tag_error_string)]
        except NotDocBook as e:
            return [Error(notdb_error_string % e)]
        return []

name = 'convention/markup-docbook'
description = 'DocBook 마크업의 짝이 맞는지 검사합니다'
checker = MarkupDocbookCheck()
