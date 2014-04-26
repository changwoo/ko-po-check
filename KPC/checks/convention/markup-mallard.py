# -*- coding: utf-8 -*-
# Mallard XML markup check

from xml.parsers.expat import ParserCreate
from xml.parsers.expat import ExpatError
from KPC.classes import Error, BaseCheck

# 메시지에 대해 XML 파서를 돌려 well formed인지 검사하고, 태그가 알려진
# Mallard 태그인지 검사한다.
# grep 'element name' mallard-1.0.rng | cut -f 2 -d'"'
known_tags = set([
    'page',
    'section',
    'info',
    'credit',
    'link',
    'title',
    'license',
    'desc',
    'revision',
    'years',
    'email',
    'name',
    'links',
    'code',
    'example',
    'media',
    'p',
    'screen',
    'quote',
    'comment',
    'figure',
    'listing',
    'note',
    'synopsis',
    'list',
    'item',
    'steps',
    'item',
    'terms',
    'item',
    'tree',
    'item',
    'table',
    'col',
    'colgroup',
    'tr',
    'thead',
    'tbody',
    'tfoot',
    'td',
    'title',
    'subtitle',
    'desc',
    'cite',
    'app',
    'code',
    'cmd',
    'output',
    'em',
    'file',
    'gui',
    'guiseq',
    'link',
    'media',
    'keyseq',
    'key',
    'span',
    'sys',
    'input',
    'var',
])

tag_error_string = 'XML 태그의 짝이 맞지 않습니다'
unknown_tag_error_string = '<%s>: 알려진 Mallard 태그가 아닙니다'


class UnknownTag(Exception):
    pass


def check_tags(name):
    if name == 'KPC_DummyTag':
        pass
    elif name[:12] == 'placeholder-':
        # old gnome-doc-utils magic
        pass
    elif name[:7] == '_:item-' or name[:7] == '_:link-':
        # newer gnome-doc-utils magic
        pass
    elif not name in known_tags:
        raise UnknownTag(name)


def start_element(name, attr):
    check_tags(name)


def end_element(name):
    check_tags(name)


class MarkupMallardCheck(BaseCheck):
    def check(self, entry, context):
        if not entry.references or not '.page:' in entry.references[0]:
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
        except UnknownTag as e:
            return [Error(unknown_tag_error_string % e)]
        return []

name = 'convention/markup-mallard'
description = 'Mallard 마크업의 짝이 맞는지 검사합니다'
checker = MarkupMallardCheck()
