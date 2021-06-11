# 기여 가이드라인

😋 먼저, semilang 프로젝트를 찾아 주신 여러분께 감사드립니다! 🥰

기여 전에 이 가이드를 모두 숙지해 주시길 부탁드립니다!

## <a id="table-of-contents">목차</a>

0. [목차](#table-of-contents)

1. [기여 전 안내 사항](#before-contribute)

2. [용어 정의](#define-terms)

3. [기여](#contribute)

    1. [기여에 대한 제한](#limit-to-contribute)

    2. [기여 종류](#kind-of-contribute)

    3. [버그 보고](#bug-report)

        1. [버그 보고서를 제출하기 전에](#before-report)

    4. [문법 아이디어 건의](#grammar-idea-suggest)

        1. [개선 제안을 제출하기 전에](#before-suggest)

    5. [풀 리퀘스트](#pull-request)

        1. [PR 기여 순서](#order-of-pull-request-process)

        2. [PR 주의사항](#caution-of-pull-request)

        3. [스타일 가이드](#style-guide)

4. [프로젝트 진행 절차](#project-workflow)

    1. [마스터 브랜치 관리 규칙](#master-branch-manage-rules)

    2. [새 문법 브랜치 관리 규칙](#new-grammar-branch-manage-rules)

    3. [새 코드 브랜치 관리 규칙](#new-code-branch-manage-rules)

    4. [커밋 가이드](#commit-guide)

5. [커뮤니티에 참여하기](#contact-our-community)

## <a id="before-contribute">기여 전 안내 사항</a>

[본 저장소][1] 에 대한 기여는 **저장소의 라이선스** ([MIT Public domain](https://opensource.org/licenses/MIT)) 에 동의한 것으로 간주하며, 이는 철회할 수
없습니다.

> ### MIT License
>
> Copyright (c) 2021 ybs1164
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## <a id="define-terms">용어 정의</a>

| 용어 | 설명 |
| :---: | :--- |
| <a id="term-repository">`저장소`</a> | [semilang repository][1] 를 의미합니다 |
| <a id="term-contribute">`기여`</a> | 저장소에 보내는 PR과, 모든 이슈 등록을 포함합니다 |
| <a id="term-semilang">`세미랭`</a> | semilang 의 일관적인 의사소통을 위한 한글 명칭입니다 |
| <a id="term-grammar">`문법`</a> | 세미랭의 문법 또는 문법을 정의한 문서를 말합니다 |
| <a id="term-code">`코드`</a> | 세미랭을 구현한 인터프리터 또는 컴파일러의 코드를 말합니다 |

## <a id="contribute">[기여](#term-contribute)</a>

### <a id="limit-to-contribute">기여에 대한 제한</a>

다음 경우에 해당되는 경우, 해당 기여는 통합이 거부될 수 있습니다.

#### <a id="grammar">[문법](#term-grammar)</a>:

- 세미콜론의 [semilang 채널][2] 에서 논의되지 않은 과도한 변경.

  단, 충분히 합리적이라면 문제 되지 않을 수 있습니다.

- 본인만의 만족을 위한 문법

- 기존의 문법을 덮어씌우거나, 기존과 호환성이 크게 벌어지는 문법.

  이 경우 semilang 채널에서 다수의 합의가 이루어져야 합니다.

- semilang 의 제작 목적을 벗어나는 문법

#### <a id="limit-to-contribute-code">[코드](#term-code):</a>

- 기여하려는 코드가 별도 **저작권**이 존재하는 경우

  (단, 일판에 대한 구상 이식은 제외하며 해당 부분은 원판 라이선스를 따릅니다.)

- 기존 코드와 지나친 호환성 파괴를 또는 과도한 통합 요구를 유발할 수 있는 경우

  (단, 관리자 판단하에 충분히 검증된 경우는 제외합니다.)

- 과도한 수준의 불필요한 변경

- 품질이 심하게 떨어지는 코드

    - 린트 경고가 너무 많은 경우

    - 주석이 많이 누락된 경우

    - [코드 포맷](#style-guide)이 통일되지 않은 경우

    - 한 파일에 800줄 이상의 코드를 한 번에 쓰거나 모듈화가 제대로 되지 않아 재사용이 어려운 경우

    - 지나치게 짧고 축약된 표현 등으로 가독성을 해친 경우

  (품질에만 있는 경우, 개선을 한 뒤 다시 PR할 경우 승인됩니다.)

### <a id="kind-of-contribute">기여 종류</a>

- [버그보고](#bug-report)

- [문법 아이디어 건의](#grammar-idea-suggest)

- [풀 리퀘스트](#pull-request)

### <a id="bug-report">버그 보고</a>

버그를 발견하셨다면 [이슈 탭](https://github.com/ybs1164/semilang/issues) 에서 버그 보고서를 제출해 주세요!

보고서를 자세히 작성해 주실수록 관리자와 semilang 프로젝트에 참여한 기여자들이 버그를 수정하는 데 도움이 됩니다.

#### <a id="before-report">버그 보고서를 제출하기 전에:</a>

- 이미 같은 이슈가 올라온 적이 있는지 확인해보세요!

  이미 해결되었거나 한창 논의 중일 수 있습니다.

    + 만약 이전에 종결 된 것과 비슷한 문제 를 발견했다면 새 이슈를 열고 본문에 원래의 닫힌 이슈에 대한 링크를 포함해 주세요.

- 일반적인 질문 및 문제 FAQ 는 [semilang 채널][2] 을 사용해 주세요.

- 가능하다면 기존의 템플릿을 이용해 주세요.

  관리자 또는 기여자들이 어떤 종류의 문제인지 확인하기 쉽습니다.

- 문제와 기대 상황을 설명해 주시고 다른 사람이 문제를 재현 할 수 있도록 추가적인 상황 정보를 포함해 주세요.

    + 상황 정보란, 터미널에서 내린 명령, 파이썬(또는 기타 런타임, 개발환경 등)의 버전, 스크린샷, 사용한 패키지 목록, 에러 메세지, 상황을 담은 gif, 참조할 외부 링크 등을 말합니다.

    + 파일 또는 코드의 경우, 스크린샷보다는 내용을 복사해서 올려 주세요.

    + 하나씩 다르게 시도해 보면서 무었이 문제인지 정확히 파악해 보세요.

- 이슈 제목은 명확하고 문제가 무었인지 한눈에 알 수 있도록 적어 주세요!

### <a id="grammar-idea-suggest">문법 아이디어 건의</a>

여러분이 생각한 완전히 새로운 기능과 기존 기능에 대한 사소한 개선 사항을 포함하여 semilang 에 대한 모든 의견을 제안해 보세요!

#### <a id="before-suggest">개선 제안을 제출하기 전에:</a>

- 여러분의 새로운 제안이 기존 버전과 문법적으로 충돌하는지 확인해 보세요.

  만약 이런 문제가 발견되더라도, 이를 보완할 만한 아이디어가 있다면 상관 없습니다.

- 정말 간단한 아이디어는 [semilang 채널][2] 을 이용하시는 것이 더 빠르게 피드백을 받을 수 있는 방법입니다.

  이슈 탭에는 단순한 질문식 건의보단 정말 문법적으로 확정되고 쓸모있다고 생각되는 기능만 건의해 주세요.

- 여러분의 새로운 기능이 왜 필요하다고 생각하시는지를 최대한 자세하고 꼼꼼하게 설명해 주세요!

- 새로 추가된 기능을 사용하는 예시를 최대한 많이 만들어 설명을 해주세요.

  이 경우, 문법적 오류를 미리 찾아내기 편하고, 이 기능이 실제로 무얼 하는지, 왜 유용한지를 한눈에 설명할 수 있습니다.

- 한 제안에는 하나의 기능만 건의해 주세요!

### <a id="pull-request">풀 리퀘스트</a>

PR로 기여하는 방법은 다음과 같습니다.

#### <a id="order-of-pull-request-process">PR 기여 순서:</a>

1. [저장소](#term-repository)를 포크합니다.

2. [마스터 브랜치][3] 또는 다른 브랜치에서 <본인 깃허브 아이디>-<브랜치 주제> 형식으로 새로운 브랜치를 생성해 주세요!

2. 로컬에서 자유롭게 코드를 수정합니다.

   단, 커밋시에 [커밋 가이드](#commit-guide) 를 지켜서 커밋해 주시면 좋습니다.

3. 배포 전 코드를 일정한 형식으로 [포맷](#style-guide)해 주세요.

4. 자신의 포크한 저장소에 푸시합니다.

5. 마지막으로, 설명과 함께 이 저장소로 PR을 보냅니다.

#### <a id="caution-of-pull-request">PR 주의사항</a>

- [코드 기여에 대한 제한](#limit-to-contribute-code) 항목에 어긋나는 내용의 PR은 거부됩니다.

- 저장소의 기존 내용과 충돌되는 내용이 많을 경우 통합이 지연될 수 있습니다.

- 마스터 브랜치에 커밋하셨을 경우, 병합이 어려워져 거부될 가능성이 높으니 본인의 브랜치를 새로 만들어 주세요.

  각 브랜치는 나중에 정식 버전이 릴리즈 될 때마다 마스터 브랜치에 병합됩니다.

  (자세한 설명은 [마스터 브랜치 관리 규칙](#master-branch-manage-rules) 을 참고해 주세요)

- [문법](#term-code) 아이디어 건의는 [이슈](https://github.com/ybs1164/semilang/issues) 또는 세미콜론의 [semilang 채널][2] 에서 주로 진행됩니다.

  풀 리퀘스트는 가급적 [코드](#term-code) 수정만을 위해 사용해 주세요.

  단, 문법 문서 공식 업데이트의 경우에는 PR을 사용하지만, 많은 분들의 합의가 필요합니다.

- semilang 프로젝트는 현재 개발중입니다.

  따라서 다양한 문법이 각 브랜치별로 토론과 시험 중에 있습니다.

  이중 시험적인 문법도 있으니 어떤 버전의 문법을 지원할지 생각해 보시는 것이 좋아요!

  현재 표준인 문법을 보고 싶으시다면, [마스터 브랜치](#master-branch-manage-rules)를 참고하시면 됩니다.

  각 시험적인 문법은 브랜치별로 나뉘어 있으니 커밋 시에 꼭 어느 브랜치, 어느 버전의 문법을 지원하는 코드인지 명시해 주세요!

  (더 자세한 사항은 [프로젝트 진행 절차](#project-workflow) 항목을 참조고해 주세요)

- [기여 전 안내 사항](#before-contribute) 에도 명시했듯이, 여러분이 제출한 모든 코드는 이 저장소 라이선스의 영향을 받습니다.

#### <a id="style-guide">스타일 가이드</a>

이 프로젝트는 일관된 코드 스타일과 git diff 오염 방지를 위해 [black](https://github.com/psf/black) 포맷터를 사용합니다.

PR을 하기 전, 마지막 커밋 전에 포맷팅을 해주세요.

##### 사용법:

black 을 설치합니다.

```sh
$ pip install black
```

다음 명령으로 파일 또는 디렉토리를 포맷할 수 있습니다.

```sh
$ black <filename>
```

커밋 전, 루트 디렉토리에서 다음 명령으로 모든 파일을 포맷할 수 있습니다.

```sh
`$ black .`
```

### <a id="project-workflow">프로젝트 진행 절차</a>

semilang 프로젝트는 지금도 개발중입니다!

semilang 의 [문법](#term-grammar)은 정식 릴리즈 된 버전과 시험중인 버전이 있습니다.

정식 버전은 [마스터 브랜치][3] 에서 찾으실 수 있고, 시험중인 버전은 각 브랜치에서 찾으실 수 있습니다.

현재 semilang 프로젝트의 모든 브랜치 목록은 [이곳](https://github.com/ybs1164/semilang/branches) 에서 보실 수 있습니다.

#### <a id="master-branch-manage-rules">마스터 브랜치 관리 규칙</a>

- [마스터 브랜치][3] 는 프로젝트 관리자가 관리하며, 동시에 semilang(문법/구현)의 최신 릴리즈를 나타냅니다.

- 마스터 브랜치는 버전을 가지며, [semver](https://semver.org/) 의 버전 표기 규칙에 기반을 둡니다.

    - 예를 들어, 정식 버전 출시 이전은 0.x.x 로 표시하며, 정식 버전은 1.x.x, 그 이후의 호환성을 깨뜨리는 업데이트가 나올 때마다 메이저 버전을 올립니다.

    - 새로 추가된 문법은 마이너 버전을 올려 표시합니다.

    - 구현체 패치, 문법 충돌 해결 등은 패치 버전을 올립니다.

    - 버전은 [깃 태그](https://git-scm.com/book/en/v2/Git-Basics-Tagging) 를 사용해 표시합니다.

- 정식 릴리즈를 할 때마다 그동안의 실험적인 브랜치들 중 채택된 것을 골라 마스터로 머지한 후 버전 태그를 붙혀 릴리즈 합니다.

#### <a id="new-grammar-branch-manage-rules">새 문법 브랜치 관리 규칙</a>

- 새 브랜치가 어떤 문법을 위한 것인지 확인하시고, 그에 맞는 명확한 이름을 정해 주세요!

- 기존의 문법에서 추가적인 문법을 넣고 싶다면 최신 [마스터 브랜치](#master-branch-manage-rules)에서 새 브랜치로 분리해 주세요.

  또는 이미 진행중인 다른 실험적인 문법에서 더 구현하고 싶으신 것이 있다면 그 브랜치에서 새 브랜치를 분리해 주세요.

- 하나의 브랜치는 하나의 문법만 다루는 것이 바람직하지만, 여러 문법을 정리하거나 동시에 관리 및 테스트 할 경우는 중간에 머지해 하나의 브랜치로 만들 수 있습니다.

    - 마찬가지로 브랜치 하나에 너무 여러 문법이 추가되었을 경우 관리를 위해 중간에 분리할 수 있습니다.

    - 새로 시작하는 브랜치 (마스터 브랜치에서 새로 만드는 브랜치) 는 가급적 문법 하나로 시작하도록 합니다.

#### <a id="new-code-branch-manage-rules">새 코드 브랜치 관리 규칙</a>

- 새 브랜치가 어떤 기능을 위한 것인지 생각 하신 후에 결정하시고, 그에 맞는 이름을 지어주세요!

- 특정 문서 브랜치에 대한 구현을 위한 것이라면 그 문서 브랜치에서 <문서 브랜치 이름>-implement 라는 이름으로 새로 브랜치를 열어 주세요.

    - 이미 있는 코드를 리팩토링 하거나 발전시키는 경우라면 새 브랜치를 만들 필요 없이 이미 존재하는 <이름>-implement 형식의 브랜치를 찾아서, 이 브랜치에서 새 브랜치를 만드세요!

    - 기반이 되는 문서 브랜치가 없는 구현 브랜치는 생성하지 말아 주세요.

      구현 브랜치를 만들기 전, 먼저 문서 브랜치를 만들어 주세요.

#### <a id="commit-guide">커밋 가이드</a>

semilang 프로젝트는 [Conventional Commits Guide](https://www.conventionalcommits.org/en/v1.0.0/) 의 커밋 메세지 규격을 따릅니다.

- 문서 브랜치에서의 type 으로는 fix, feat, experimental 을 허용합니다.

    - fix 는 기존의 문법적 오류를 해결한 경우,

  feat 는 새로운 문법적 기능을 추가한 경우 또는 개선한 경우,

  experimental 은 실험적인 기능을 도입한 커밋을 의미합니다.

  (원래라면 docs 가 되겠지만, semilang 의 경우 문법 문서 자체가 메인 파일이고, 업데이트가 진행되는 주체이자 오류가 발생할 수 있는 대상이기 대문에 docs 대신 다음의 type 을 가집니다)

- 코드 브랜치에서는 fix, feat, perf, test, style, refactor, build 를 허용합니다.

    - fix 는 기존 구현체의 버그를 수정한 경우,

  feat 는 새로운 문법에 대한 구현체를 추가했을 경우,

  나머지 type 들에 대한 설명은 [앵귤러 기여 가이드](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#type) 를 참고해 주세요.

다만, Conventional Commits Guide 적용은 강제적이지 않으며, 이에 따르지 않는 커밋 메세지도 가독성만 있다면 허용합니다.

- 하지만 어느 경우든 커밋 본문에는 어떤 부분이 수정되었는지, 왜 수정되었는지, 이 수정이 앞으로 어떤 영향을 미칠 수 있는지를 상세하게 써 주셔야 합니다.

### <a id="contact-our-community">커뮤니티에 참여하기</a>

[세미콜론 서버](https://discord.gg/yjhTbmjmbP)
의 [semilang](2) 채널로 오시면 이 프로젝트에 대한 다양하고 자세한 지원을 받으실 수 있습니다!

- 간단한 질문 및 Q&A 답변

- 최신 semilang 프로젝트 진행 상황

등에 대한 정보를 얻으실 수 있으며, 이슈 탭보다 답변이 빠릅니다.

이 프로젝트에 대한 자세한 질문도 이곳에서 모두 하실 수 있습니다!

[1]: https://github.com/ybs1164/semilang

[comment]: <> (this repository)

[2]: https://discord.com/channels/662649985996816395/799611643142995968

[comment]: <> (semilang channel)

[3]: https://github.com/ybs1164/semilang/tree/main

[comment]: <> (master branch)