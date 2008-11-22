# -*- encoding: utf-8 -*-

import string,re

name = "language/spell"
description = '흔히 하는 맞춤법 오류를 찾아냅니다'

# 의존명사를 위한 -할 형태의 동사 모음
verbs_re = u'('+string.join([
    u'가져올',
    u'갈',
    u'걸',
    u'고칠'
    u'나타날',
    u'내릴',
    u'놓일',
    u'되돌릴',
    u'만들',
    u'바꿀',
    u'보낼',
    u'볼',
    u'생길',
    u'시킬',
    u'쓸',
    u'알',
    u'얻어낼',
    u'얻을',
    u'없앨',
    u'열',
    u'올',
    u'일',
    u'읽어들일',
    u'읽을',
    u'있을',
    u'잠글',
    u'지울',
    u'찾을',
    u'할',
    ], '|')+u')'

variations_re = u'(있다|없다|있습니다|없습니다|있는|없는|있게|없게)'

# 조사 모음
chosa_re = '('+string.join([
    u'가',u'이',u'이\(가\)',
    u'를',u'을',u'을\(를\)',
    u'는',u'은',u'은\(는\)',
    u'로',u'으로',u'\(으\)로',
    u'로서',u'으로서',u'\(으\)로서',
    u'로써',u'으로써',u'\(으\)로써',
    u'로부터',u'으로부터',u'\(으\)로부터',
    u'라는',u'이라는',u'\(이\)라는',
    u'의', u'도', u'에', u'에서', u'만', u'부터',
    ], '|')+')'

def test_noun_suffix(str):
    if (str[-1] != u'슴'):
        return 1
    elif ((ord(str[-2]) - 0xac00) % 28 == 20):
        return 0
    elif (str[-2] == u'없'):
        return 0
    else:
        return 1
    

misspell_data = [
    { 're':    re.compile(u'(않\s*(한|함|합니다|된|됨|됩니다))'),
      'error': u'\"%s\": 짧은 부정문에서는 \'않\'이 아니라 \'안\'을 씁니다' },
    { 're':    re.compile(u'(읍니다)'),
      'error': u'\"%s\": \'읍니다\'가 아니라 \'습니다\'입니다' },
    { 're':    re.compile(u'([^\s]+슴)([\s\.\,\?]|$)'),
      'func':  test_noun_suffix,
      'error': u'\"%s\": \'슴\'이 아니라 \'음\'입니다' },
    { 're':    re.compile(u'('+verbs_re+u'수(가|도|는)?\s'+')'),
      'error': u'\"%s\": 의존 명사는 띄어 써야 합니다' },
    { 're':    re.compile(u'('+verbs_re+u'\s*수(있|없)'+')'),
      'error': u'\"%s\": 의존 명사는 띄어 써야 합니다' },
    { 're':    re.compile(u'('+verbs_re+u'때(가|도|는)?\s'+')'),
      'error': u'\"%s\": \'~할 때\'라고 띄어 써야 합니다' },
    { 're':    re.compile(u'([0-9A-Za-z-+\`\'\"()%_]+ '+chosa_re+u')\s+'),
      'error': u'\"%s\": 조사는 체언에 붙여 써야 합니다' },
]

def check(entry):
    msgid = entry.msgid
    msgstr = entry.msgstr
    ret = 1
    errmsg = ""
    for data in misspell_data:
        misspell_re = data['re']
        misspell_error = data['error']
        str = msgstr
        while 1:
            mo = misspell_re.search(str)
            if mo:
                if (data.has_key('func') and data['func'](mo.group(1))):
                    str = str[mo.end():]
                    continue
                ret = 0
                if errmsg:
                    errmsg += '\n'
                errmsg += misspell_error % mo.group(1)
                str = str[mo.end():]
            else:
                break;
    return (ret, errmsg)    

if __name__ == '__main__':
    import sys
    class entry:
        pass
    entry.msgid = sys.stdin.readline()
    entry.msgstr = sys.stdin.readline()
    t,e = check(entry)
    if not t:
        print e
    else:
        print 'Success'
