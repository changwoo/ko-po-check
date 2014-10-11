# -*- coding: utf-8 -*-
# Mallard XML markup check

from xml.parsers.expat import ParserCreate
from xml.parsers.expat import ExpatError
from KPC.classes import Error, BaseCheck

# 메시지에 대해 XML 파서를 돌려 well formed인지 검사하고, 태그가 알려진
# Mallard 태그인지 검사한다.
# grep 'element name' mallard-1.0.rng | cut -f 2 -d'"'
known_tags = set([
    'app',
    'cite',
    'cmd',
    'code',
    'col',
    'colgroup',
    'comment',
    'credit',
    'desc',
    'em',
    'email',
    'example',
    'figure',
    'file',
    'gui',
    'guiseq',
    'info',
    'input',
    'item',
    'key',
    'keyseq',
    'license',
    'link',
    'links',
    'list',
    'listing',
    'media',
    'name',
    'note',
    'output',
    'p',
    'page',
    'quote',
    'revision',
    'screen',
    'section',
    'span',
    'steps',
    'subtitle',
    'synopsis',
    'sys',
    'table',
    'tbody',
    'td',
    'terms',
    'tfoot',
    'thead',
    'title',
    'tr',
    'tree',
    'var',
    'years',
])

tag_error_string = 'XML 태그의 짝이 맞지 않습니다'
unknown_tag_error_string = '<%s>: 알려진 Mallard 태그가 아닙니다'


class UnknownTag(Exception):
    pass


def check_tags(name):
    if name.startswith('_:'):
        # newer gnome-doc-utils magic
        pass
    elif name.startswith('placeholder-'):
        # old gnome-doc-utils magic
        pass
    elif name not in known_tags:
        raise UnknownTag(name)


def start_element(name, attr):
    check_tags(name)


def end_element(name):
    check_tags(name)


class MarkupMallardCheck(BaseCheck):
    def check(self, entry, context):
        if not entry.references or '.page:' not in entry.references[0]:
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
            parser.Parse('<_:ko-po-check>' + msgstr + '</_:ko-po-check>')
        except ExpatError as e:
            return [Error(tag_error_string)]
        except UnknownTag as e:
            return [Error(unknown_tag_error_string % e)]
        return []

name = 'convention/markup-mallard'
description = 'Mallard 마크업의 짝이 맞는지 검사합니다'
checker = MarkupMallardCheck()
