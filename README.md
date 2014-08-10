ko-po-check - 한국어 PO 파일 검사툴

이 프로그램은 한국어 메시지 번역 파일(PO 파일)에서 흔히 범하는
실수들을 찾아내는 프로그램입니다.

이 프로그램은 파이썬 3.0 이상에서 동작합니다. 일반적인 파이썬 모듈과
마찬가지 방법으로 설치할 수 있습니다.

    $ python3 setup.py install

또는 pip나 easy_install을 이용해 PyPI에서 ko-po-check를 설치하셔도
됩니다.

    $ pip install ko-po-check

이 프로그램은 GNU General Public License version 3 혹은 그 이후
버전으로 배포합니다. 정확한 라이선스는 COPYING 파일에서 볼 수
있습니다.

도와 주신 분들은 소스 코드의 THANKS 파일에 들어 있습니다. 이 프로그램
개발에 관한 정보는 github의 프로젝트 페이지에 있습니다. 제안 사항이나
문제점은 다음 프로젝트 페이지로 알려 주십시오.

프로젝트 페이지: https://github.com/changwoo/ko-po-check

문제점: https://github.com/changwoo/ko-po-check/issues

Package Index (PyPI)
   https://pypi.python.org/pypi/ko-po-check


자주 묻는 질문 (1) 제대로 된 번역이 확실한데 왜 에러가 나오는가
--------------------------------------------------------

사용자 중에서 "ko-po-check에서 어떤 에러가 발생했는데 번역은
올바르다"라고 피드백을 하는 경우가 종종 있습니다.

불행히도 이 프로그램에서 보고하는 문제점 중에는 문제점이 아닌데도
문제점으로 보고되는, 즉 false alarm이 있을 수밖에 없고 결국 번역을
어떻게 할지에 대한 판단은 본인이 해야 합니다. 가능한한 틀린 문제점
보고를 줄이려고 노력할 것이지만 100% 정확한 오류 검색은 가능하지
않습니다.

만약 틀린 문제점 보고가 지나치게 많고 줄일 방법이 마땅히 없다면, 아예
문제점을 보고하지 않는 편이 좋을 것입니다. 적절한 선을 유지하는 게
중요합니다.

심지어 어떤 사용자는 이러한 틀린 문제점 보고 때문에 이 프로그램이
쓸모가 없다거나 유용성이 많이 떨어진다고 섣불리 말하기도 합니다. 하지만
실제 메시지 번역에서는 그렇지 않습니다. 이 프로그램은 수년간 많은
메시지 번역에 활용되어 왔지만, 실제 메시지에서 이런 틀린 문제점 보고는
전체에 비하면 극히 적은 수에 불과합니다.


자주 묻는 질문 (2) 무슨 무슨 오역을 잡아내는 규칙이 없으니까 추가하자
------------------------------------------------------------

새로운 규칙을 제안하거나 기능을 보강하는 건의 사항은 환영합니다. 하지만
이 프로그램은 널리 쓰이는 실수를 잡아낼 뿐이지 모든 오역을 잡아낼 수는
없습니다. 구현이 충분히 가능한지, 도움이 되는지 검토해 주십시오.

앞의 경우처럼, 올바른 경우에 대해서도 오류를 너무 많이 표시하면
부작용이 너무 큽니다. 또 실제로 거의 발생하지 않는 오류는 추가해 봐야
별 의미가 없습니다.

즉, 새로운 기능의 추가는 기존에 충분히 많은 사례가 있고 검사하는 게
유용하다는 판단이 먼저 있어야 할 일이지 틀릴 수 있는 가능한 모든
케이스를 상상해 가면서 추가하는 건 바람직하지 않습니다.


자주 묻는 질문 (3) 어떤 용어보다 다른 용어가 낫지 않나
-----------------------------------------------

ko-po-check에서 용어 관련 검사에서 사용되는 용어는 개인적인 선호로
결정하지 않았고, 보통 많이 사용되는 용어가 무엇인가에 대해 조사를 통해
결정되었습니다. 다른 OS에서 사용된 용어, 언론이나 출판에서 많이
사용되고 있는 용어 따위입니다.

그럼에도 불구하고 ko-po-check에서 사용되는 용어에 대해 맞냐 틀리냐
토론하려는 분이 종종 있습니다. 그 동안의 메시지 번역 경험에 따라
말씀드리면, 번역에 사용할 단어를 가지고 의미를 분석하는 일은 시간만
소모하고 아무런 결론도 나지 않습니다. 보통 자기가 선호하는 용어에
논리를 끼워맞추게 됩니다. 여기 사용되는 용어는 일관성을 위해 어떤
용어를 선택했을 뿐입니다.

다른 용어를 선호하신다면 용어 검사 관련 메시지를 무시해 주시면 됩니다.
