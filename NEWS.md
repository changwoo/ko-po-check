버전 0.98.0
==========

  * 새로운 검사 규칙

    * convention/do-not-translate: 번역하지 말라는 안내가 쓰여진 경우 검사

  * 개선

    * convention/markup-docbook: 최근 gnome-doc-utils의 placeholder tag 반영

    * convention/markup-docbook: CDATA에 bracket 들어 있는 경우에 대한 처리

    * convention/strftime: C99 strftime() modifiers 추가

    * langauge/consistency: 원문과 같이 유니코드 따옴표 사용하기 추가

    * terminology/{common-labels,desktop-common}: '...'대신 U+2026 사용할 경우 대응

	* terminology/word-guide: "헤더 표시줄" -> "헤더 모음"으로 용어 안내

	* language/badstyle: 복수형 패턴 예외로 '번들'+조사 추가

버전 0.97.0
===========

  * 개선

    * language/punctuation: 괄호 앞 띄어쓰기 검사 삭제 - 맞춤법 상에서는 붙여
      써야 맞지만, 실제로 단어가 아니라 문장에 부가 설명으로 붙은 괄호가 많아
      붙여 쓰기가 부적합할 수도 있다.

    * language/spell: 잘못된 알림 최소화

    * terminology/desktop-common: 용어 추가

    * terminology/help-license: 오타 수정

    * terminology/word-guide: 용어 추가

  * 문제점 개선

    * terminology/desktop-common: 마지막 글자가 밑줄일 경우 access key 오류 바로잡음

버전 0.96.2
===========

  * 새로운 검사 규칙

    * terminology/help-license: 도움말 문서의 법률 정보에 많이 사용하는 문구 번역 통일

  * 개선

    * convention/markup-mallard: tag 목록 정리

    * language/badstyle: 어색한 표현 추가

    * language/punctuation: 번역문에 세미콜론 사용하는 경우 검사


버전 0.96.0
===========

  * 개선

    * 내부 구조 변경 - PO entry의 여러가지 flag를 더 유연하게 처리하도록 고정된 값에서 set으로 바꿈

    * convention/markup-mallard: gnome-doc-utils에서 만드는 '_:'로 시작하는 placeholder 인식

    * language/josa-alternative: 따옴표로 U+2019 또는 U+201D를 사용했을 때 처리

    * language/punctuation: 괄호 앞에 띄어 쓴 strftime 포맷은 허용

    * language/spell: 띄어 쓴 조사 검사할 때 유니코드 따옴표 고려

    * language/spell: 띄어 쓴 조사가 메시지 끝인 경우 추가

    * language/spell: 단위 명사를 아라비아 숫자와 띄어 쓴 경우 추가, 띄어 쓰기를 허용하지만 보통 붙여 쓴다

    * language/spell: '읍니다' => '습니다' 예외 추가

    * terminology/gschema: 마침표 없는 경우 추가

    * terminology/word-guide: 용어 추가

    * convention/extra-space: 스페이스 외에 다른 공백 문자 검사

    * convention/markup-docbook: 태그 추가


버전 0.95.5
===========

  * 문제점 개선

    * terminology/word-guide: 용어 오타 바로잡음

버전 0.95.4
===========

  * 새로운 검사 규칙

    * convention/team-common: 헤더에 정치적 문구를 넣는 경우 검사

      여러분들의 애국심을 존중하지만, 번역 정보는 정치적인 주장을 하는 곳이 아닙니다.

    * convention/extra-space: 불필요한 공백 문자를 뒤에 덧붙이는 경우 검사

  * 개선

    * terminology/word-guide: 용어 추가

    * terminology/gschema: 원문 대소문자만 다른 경우 처리

    * convention/common-header: 번역자 이름이나 메일을 초기 기본값에서 바꾸지 않은 경우 검사


버전 0.95.3
===========

  * 새로운 검사 규칙

    * convention/desktop-keyword: freedesktop.org desktop 엔트리의 Keyword 번역 확인

    * language/gschema: gschema에서 많이 사용하는 설명문의 번역이 통일되었는지 검사

  * 개선

    * convention/access-key: accesskey에서 이름 변경

    * convention/access-key: 접근키 예외 추가 - XML entity 형태(&blah;)

    * convention/typo-incomplete: typoincomplete에서 이름 변경

  * 문제점 개선

    * PyPI를 위한 메타데이터 추가

    * flake8 발견한 코드 문제 수정

    * 기타 오류 수정


버전 0.95.2
===========

  * 개선

    * language/spell: 조사 목록 업데이트

    * language/josa-alternative: 잘못된 메시지 바로잡음

    * language/punctuation: 괄호 앞 띄어쓰기 검사시 괄호 뒤 공백문자가 아닌 모든 문자 검사

    * convention/strftime: 시각 표시에 콜론 대신 U+2236 문자 사용하는 경우 고려

    * convention/accesskey: 접근키 예외 추가 - 소문자로 시작하는 경우 & URL로 보이는 경우

  * 버그 수정

    * 기타 오류 수정


버전 0.95.1
===========

  * 개선

    * language/badstyle: 규칙 추가

    * language/josa-alternative: chosaalternative에서 이름 변경.

    * language/josa-alternative: 파이썬 포맷 스트링도 검사

    * terminology/word-guide: 용어 업데이트

    * convention/markup-docbook: 최근 gnome-doc-utils 고려

    * convention/markup-mallard: 최근 gnome-doc-utils 고려

  * 기타

    * 설치에서 Python 버전이 3.x인지 검사


버전 0.95.0
===========

  * 이제부터 Python 버전 3.x 사용

  * 새로운 검사 규칙

    * language/badstyle: 번역체 등 바람직하지 못한 스타일의 번역 검색

  * 개선

    * terminology/word-guide: gnomeguide에서 이름 변경. 그놈 전용이라는 오해 방지.

    * terminology/word-guide: 용어 업데이트

    * terminology/desktop-commons: gnomeui에서 이름 변경.  그놈 전용이라는 오해 방지.

    * convention/strftime: 날짜/시각 형식 추가

  * 기타

    * terminology/desktop-commons: test case 추가


버전 0.94.2
===========

  * 개선

    * convention/markup-docbook: 태그 추가

    * language/spell: 조사 목록 추가

    * terminology/gnomeguide: 단어 추가

    * convention/strftime: 각종 strftime() 플래그를 사용한 경우 지원

    * convention/header-comment: 헤더의 번역자 이름에 공백이 추가로 들어갔을 경우 무시

  * 기타

    * 테스트 케이스 추가 및 정리

    * 기타 정리

    * Trove 패키지 분류 추가


버전 0.94.1
===========

  * 새로운 검사 규칙:

    * convention/header-comment:

    * PO-Revision-Date에 기록된 년도를 헤더 코멘트에 안 쓴 경우에 대해 검사

  * 개선

    * language/punctuation: 괄호 앞에 공백은 한국어에서만 문제로 취급

    * language/gnomeguide: 용어 업데이트

    * 내부 테스트케이스 관련 버그 수정


버전 0.94.0
===========

  * 새로운 검사 규칙:

    * convention/markup-mallard: Mallard 형식의 그놈 도움말 번역문에서 Mallard XML 태그가 올바른지 검사

    * language/punctuation: 맞춤법에 따른 올바른 기호 사용에 대한 검사

    * 현재 괄호 앞에 띄어 쓴 경우에 대해 검사: 한국어 맞춤법에서는 괄호 앞에 띄어쓰지 않음

  * 기타

    * github를 프로젝트 사이트로 사용


버전 0.93.0
===========

  * 개선

    * 용어 업데이트


버전 0.92.0
===========

  * 개선

    * 용어 업데이트

    * convention/chosaalternative: 와/과 조사 추가

    * convention/accesskey, terminology/common-labels: GConf schema 파일을 고려한 부분을 GSettings schema 파일도 적용

    * convention/datetime: 시간/날짜 형식 추가


버전 0.91.2
===========

  * 개선

    * 용어 업데이트

  * 새로운 검사 규칙:

    * terminology/common-labels: 전형적인 번역문을 일관적으로 유지

  * 버그 수정

    * PO 파일 헤더에 charset이 없을 경우 애러 발생 수정

    * XML character entity가 들어간 문자열은 단축키 검사 예외


버전 0.91.1
===========

  * 개선

    * 용어 업데이트

    * convention/gnome-team: 헤더의 Language-Team 필드에 없어진 KLDP.net의 메일링 리스트가 있으면 새 리스트 주소 안내

  * 새로운 검사 규칙:

    * convention/datetime: strftime() 시간/날짜 형식을 한국어 관습에 맞게 번역했는지 검사

  * 기타

    * 용어 변경: mnemonic -> access key

    * convention/gnome-team: GNOME Korea 이면서 메일이 틀린 경우 검사


버전 0.91.0
===========

(0.90.4에서 배포할 파일이 잘못 만들어져 새 파일들이 누락되었습니다.)

  * 개선

    * language/consistency: 문장 부호로 ... 대신 유니코드 U+2026 사용했을 경우 처리

  * 새로운 검사 규칙:

    * convention/common-header: 헤더에 쓰는 여러가지 사항이 올바른지 검사

    * terminology/libegg: (그놈 프로젝트 다수에서 사용하는) libegg에서 가져온 코드에 대해 통일된 번역인지 검사

  * 기타

    * 내부 구조 변화: 검사 규칙 인터페이스로 KPC.classes의 클래스 사용

    * convention/accesskey: convention/mnemonic에서 이름 변경

    * language/consistency: convention/consistency에서 이름 변경


버전 0.90.4
===========

  * 개선

    * terminology/gnomeui, terminology/gnomeguide: 용어 업데이트

    * convention/kde: msgctx를 사용하는 최근의 KDE 형식을 처리

  * 새로운 검사 규칙:

    * convention/gnome-team: 헤더의 Language-Team 필드에 없어진 KLDP.net의 메일링 리스트가 있으면 새 리스트 주소 안내


버전 0.90.3
===========

  * 개선

    * 용어 업데이트

    * 누락된 Docbook tag 추가


버전 0.90.2
===========

  * 버그 수정

    * Pango 마크업이 여러 줄에 걸쳐 있는 경우 맞지 않는다고 검사하는 문제 바로잡음

    * 버전 표시 잘못 나오는 현상 바로잡음

  * 개선

    * 용어 업데이트


버전 0.90.1
===========

  * 새로운 검사 규칙:

    * Docbook XML 마크업 검사 (gnome-doc-utils 혹은 poxml을 통해 변환된 문서)

  * 버그 수정

    * 파일 경로에 '/' 대신 os.sep 사용

    * 두 가지 용어 규칙이 "paste"를 붙여넣기/붙여 넣기로 모순되게 검사하는 문제 바로잡음

    * Pango 마크업이 문자열 중간에 오는 경우 맞지 않는다고 검사하는 문제 바로잡음

    * Pango 마크업이 여러 개 등장하는 경우에도 1개만 검사하는 문제 바로잡음

  * 개선

    * 용어 업데이트

    * 접근키 검사에 XML entity가 잡히지 않도록 일부 예외 사항을 더 추가.

    * 끝나는 문장 부호 검사에 etc.나 a.m. 따위가 잡히지 않도록 예외 추가


버전 0.90.0
===========

  * distutils로 변경

    * 필요가 없어진 디버깅용 --moduledir, --checksdir 옵션 삭제

  * 개선

    * 그놈 2.26 대비 새로운 용어 업데이트

  * 기타

    * 라이센스를 GPL 버전 3으로 바꿈

    * 애러 메세지 변경: mnemonic -> 접근키

    * 검사 목록을 보는 --list 옵션 추가 (디버깅용)


버전 0.10
=========

  * 버그 수정

    * msgctxt 항목이 여러 줄일 경우 파싱 애러 수정

    * 테스트 케이스 애러 수정

  * 개선

    * 새로운 용어 업데이트

    * 디버깅용 --filters 옵션 추가


버전 0.9
========

  * 개선

    * PO 파일의 msgctxt 파싱 추가

    * 새로운 용어 업데이트


버전 0.8
========

  * 버그 수정

    * 복수형 번역에서 줄번호를 파싱하지 않았기 때문에 복수형 번역에서 문제가 있을 경우에 예외를 발생시키는 현상 수정.

  * 개선

    * 코드 정리 - 모두 UTF8 string 사용

    * GNOME 용어: 새로운 GNOME 용어 업데이트

    * 불완전한 음절 검사: - gdm 예외 추가 ("ㅇ-ㅎ:한국어" 등)


버전 0.7
========

  * 개선

    * GNOME 용어 추가


버전 0.6
========

  * 새로운 검사 규칙:

    * markup이 맞는지 검사하는 기능 : pango markup이 들어 있는 메세지를 번역하는 데 이용

    * mnemonic이 틀리거나 mnemonic을 빼먹은 경우에 대한 검사 기능

    * 불완전한 음절 검사: 대부분이 오타로 생기는 불완전한 한글자모를 검사

  * 개선

    * GNOME 용어 추가


버전 0.5
========

  * 새로운 검사 규칙:

    * 몇 가지 단어에 대해서 정해진 번역을 사용하지 않은 경우 검사.  (예: Find -> 찾기)

    * msgid와 msgstr 사이의 일관성 (예: msgid가 ":"으로 끝나면 번역문도 ":"로 끝난다)

  * 용어 검사 일부 변경


버전 0.4
========

  * 새로운 검사 규칙:

    * 두벌식 오타 검사: ~빈다(~ㅂ니다), 밍나합니다(미안합니다), 살마(사람), 거싱(것이)

  * 내부 코드를 EUC-KR에서 UTF-8 코드로 변경.


버전 0.3
========

  * 새로운 검사 규칙:

    * '~ㅆ음'을 '~ㅆ슴' 따위로 쓴 경우.

  * 개선:

    * KDE에서 "_:"로 시작하는 메세지가 "_:"로 시작하도록 번역된 경우 검사

    * 어색한 한자어 번역 찾아내기

  * 문서화 시작

  * 내부 인코딩을 유니코드로 변경.


버전 0.2
========

  * 새로운 검사 규칙:

    * 조사 띄어 쓰기

    * "~할 때" 띄어 쓰기

    * GNOME 프로그램에서 "translator_credits"를 번역한 경우

    * KDE 프로그램에서 "_: EMAIL OF TRANSLTORS..." 혹은 "_: NAME OF TRANSLTORS"를 그대로 번역한 경우

  * 로케일 정보를 읽어 해당 로케일의 문자셋으로 메세지를 출력

  * parse error시 줄 번호 표시

  * 그 외에 여러 가지 버그 수정


버전 0.1
========

  * 최초 릴리즈
