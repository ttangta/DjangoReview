## 1. 학습 목표 요약
![학습 목표 키워드](./images/01_학습%20목표%20요약.png)

1. 웹 브라우저는 `클라이언트` 로서 인터넷 상의 컴퓨터에 `요청(Request)`을 보냅니다.
2. 이 `요청`을 받은 `서버`는 `요청`에 따라 알맞은 `응답(Response)`을 보냅니다.
3. 이러한 형태로 제공되는 서비스를 `웹 애플리케이션`이라고 하며, 이를 빠르게 개발할 수 있도록 도와주는 도구가 `웹 프레임워크`입니다.

<br>
<hr>
<br>

## 2. 웹 브라우저 & 웹 애플리케이션

### 웹 브라우저
웹 브라우저는 사용자가 웹을 이용하도록 돕는 **클라이언트 프로그램**

브라우저는 주소를 받아 서버에 HTTP(S) 요청을 보내고, 응답으로 받은 HTML / CSS / JavaScript / 이미지 등을 화면에 표시

사용자의 동작(이벤트)도 처리. 

|역할|설명|
|---|---|
|요청 보내기 (Request)|URL에 해당하는 서버에 HTTP(S) 요청을 보냄|
|응답 받기|서버의 응답과 상태 코드, 응답 헤더 등을 받음|
|콘텐츠 해석하기|HTML, CSS, JavaScript, 이미지 등의 형식에 맞게 처리|
|화면 그리기|문서 구조와 스타일을 계산해 화면에 표시|
|사용자 동작 처리|클릭, 입력, 스크롤, 키보드 동작 등을 웹 페이지에 전달|
|웹 보안 적용|출처가 다른 페이지끼리 데이터에 접근하는 것을 제한하는 등 보안 규칙을 적용|

#### 브라우저의 주요 구성 요소
- **브라우저 UI** : 주소창, 탭, 뒤로 가기 버튼처럼 **웹 페이지 바깥의 기능을 담당**
- **네트워크 처리 기능** : 서버에 요청을 보내고 응답을 받음
- **렌더링 엔진** : HTML과 CSS를 처리해 화면에 표시
- **JavaScript 엔진** : 브라우저에서 JavaScript 코드 실행
- **저장 기능** : 쿠키, `localStorage`, `sessionStorage`, IndexedDB 등 관리

#### 브라우저와 웹 보완

브라우저는 서로 다른 웹사이트의 데이터가 함부로 섞이지 않도록

동일 출처 정책(Same-Origin Policy)을 적용. 

- 출처는 일반적으로 URL의 프로토콜/호스트/포트를 기준으로 구분

```txt
예시 상황:

https://site-a.com 에서 JavaScript가 https://site-b.com 을 마음대로 읽지 못하게 제한할 수 있음

다른 출처의 데이터 접근을 허용하려면 서버가 CORS 관련 응답 헤더로 허용 범위를 알려줘야 함.

즉, CORS는 서버가 허용 정보를 응답하고 브라우저가 그 규칙을 적용하는 방식
```

#### 브라우저가 관리하는 쿠키와 저장소
- **쿠키** : 서버가 설정할 수 있고, 조건에 맞으면 브라우저가 이후 요청에 함께 보냄.
- `localStorage` : 같은 출처에서 접근할 수 있고 브라우저를 닫았다 다시 열어도 데이터가 남을 수 있음
- `sessionStorage` : 같은 출처에서 접근하며, 일반적으로 해당 탭의 세션이 끝나면 데이터 사라짐

<hr>

### 웹 애플리케이션
웝 애플리케이션(Web Application)은 **웹 기술과 네트워크를 통해 사용자에게 제공하는 소프트웨어**

사용자는 보통 브라우저로 접속, 웹 애플리케이션은 요청을 처리해 HTML이나 JSON 같은 응답을 돌려줌

<br>

#### 웹 애플리케이션의 일반적인 구성

|구성 요소|역할|
|---|---|
|브라우저·프론트엔드|화면을 표시하고 사용자 입력을 처리함. 서버에 요청을 전달|
|웹 서버·백엔드 애플리케이션|URL과 요청을 처리하고, 필요한 로직을 수행해 응답을 생성|
|데이터베이스|데이터를 저장하고 조회|

<br>

#### 웹 애플리케이션 화면 제공 방식


**서버 사이드 렌더링 (SSR)**

서버가 데이터를 가져와 HTML을 만들어 브라우저에게 전달
```txt
브라우저 요청 -> 서버가 HTML 생성 -> 브라우저가 HTML 표시
```

**클라이언트 사이드 렌더링 (CSR)**

서버가 HTML과 JavaScript 파일 등을 전달하고, 브라우저에서 실행되는 JavaScript가 데이터를 받아 화면 구성

<br>

**다중 페이지 애플리케이션 (MPA) vs 단일 페이지 애플리케이션 (SPA)**

- **MPA** : 페이지를 이동할 때 브라우저가 새 문서를 서버에 요청하는 방식
- **SPA** : 처음 문서를 받은 뒤, JavaScript가 필요한 데이터와 화면만 갱신하는 방식

|SSR & CSR|MPA & SPA|
|---|---|
|화면을 어디서 만들지|페이지 이동과 문서 갱신을 어떻게 할지|

<br>

### 핵심 정리
웹 브라우저는 사용자의 요청을 HTTP(S)로 서버에 전달하고, 응답으로 받은 HTML·CSS·JavaScript 등을 해석해 화면을 표시하는 클라이언트

웹 애플리케이션은 브라우저와 서버가 네트워크로 통신하며 기능을 제공하는 소프트웨어

보통 프론트엔드는 화면과 사용자 입력을 처리하고, 백엔드는 요청에 따라 비즈니스 로직을 수행하고 데이터베이스오 통신한 뒤 HTML이나 JSON 등을 응답

<br>
<hr>
<br>

## 3. 클라이언트와 서버

### 클라이언트 (Client)

클라이언트는 **서버에 필요한 기능이나 데이터를 요청하는 쪽.** 웹에서는 웹 브라우저가 대표적인 클라이언트

### 서버 (Server)

서버는 **클라이언트의 요청을 받아 처리하고, 결과를 응답하는 쪽.** 요청에 맞는 웹 페이지나 데이터 데이터베이스에서 조회하거나, 새로운 데이터를 데이터베이스에 저장하는 작업 처리

### 웹에서 요청·응답 흐름
1. 브라우저(클라이언트)가 서버에 게시글 목록을 요청
2. 서버가 요청에 맞는 데이터를 조회하거나 처리
3. 서버가 결과를 응답으로 보냄
4. 브라우저가 응답을 화면에 표시
- **클라이언트와 서버는** 컴퓨터의 종류가 아니라 **통신에서 맡은 역할**을 가리킴

<br>
<hr>
<br>

## 4. Frontend & Backend

웹 애플리케이션은 크게 **사용자가 보고 조작하는 부분** 과 **요청을 처리하고 데이터를 관리하는 부분** 으로 구분

### Frontend
사용자가 직접 보고 조작하는 화면과 기능을 만드는 영역
- 화면을 표시하고 디자인
- 버튼 클릭, 입력, 페이지 이동 같은 동작 처리
- 필요한 데이터를 Backend에 요청하고, 응답받은 결과를 화면에 표시

### Backend

화면 뒤에서 요청을 처리하는 영역
- 요청이 올바른지 확인
- 로그인, 권한, 게시글 작성 같은 서비스 로직을 처리
- 필요한 데이터를 데이터베이스에서 조회하거나 저장
- 처리 결과를 Frontend에 응답

### 게시글 목록을 불러오는 예시

1. Frontend가 게시글 목록을 요청
2. Backend가 요청을 받아 게시글 데이터 조회
3. Backend가 조회 결과를 응답
4. Frontend가 응답받은 게시글을 화면에 표시

<br>
<hr>
<br>

## 5. Framework -> Web Framework -> Django

세 용어는 **넓은 개념에서 구체적인 예로 좁아지는 관계**

```txt
Framework
└── Web Framework
    └── Django
```

### Framework (프레임워크)

**애플리케이션을 만들 때 필요한 기본 구조와 공통 기능을 제공하는 틀**

개발자는 모든 기능을 처음부터 만들기보다, 프레임워크가 마련한 구조 안에서 필요한 코드 작성

프레임워크가 전체 흐름과 구조를 제공하고, 개발자가 그 흐름에 맞춰 기능을 채움

<br>

### Web Framework (웹 프레임워크)
웹 애플리케이션을 만들기 위한 플레임워크

웹 요청을 받아 처리하고 응답을 돌려주는 데 필요한 기능 제공
- URL에 따라 처리할 코드 연결
- 요청과 응답 처리
- 데이터베이스 연결과 데이터 조회
- HTML 또는 JSON 응답 생성
- 로그인, 입력값 검증 등 공통 기능 지원

<br>

### Django 
Python으로 웹 애플리케이션을 개발할 수 있게 도와주는 Web Framework

- **URLconf** : 요청 URL에 맞는 View 연결
- **View** : 요청을 처리하고 응답 준비
- **Modle/ORM** : 데이터베이스의 데이터를 다루도록 도움
- **Template** : HTML 화면을 만드는 데 활용

[각 용어의 관계 도식화](./images/02_Framework%20용어%20관계%20정리.png)
 
<br>
<hr>
<br>

## 6. 가상 환경 (Virtual Environment)

가상 환경은 **하나의 컴퓨터에서 Python 프로젝트마다 독립적인 실행 환경을 구성하여 사용**하는 기술.

프로젝트별로 Python 실행 파일과 외부 라이브러리(패키지)를 분리하여 관리할 수 있으며, **서로 다른 프로젝트 간의 의존성 충돌을 방지**

- **독립성** : 프로젝트마다 별도의 Python 환경을 구성할 수 있음
- **의존성 관리** : 프로젝트별로 필요한 라이브러리와 버전을 관리할 수 있음
- **환경 보호** : 다른 프로젝트나 시스템 전역의 Python 패키지에 영향을 주지 않음

단, 가상 환경은 새로운 Python 버전을 설치하는 기능이 아니며, **컴퓨터에 이미 설치된(Python Global) 기반으로 생성**

<br>

### 가상 환경이 필요한 이유

**1. 프로젝트 간 라이브러리 충돌 방지**

여러 프로젝트에서 **서로 다른 버전의 라이브러리를 사용하는 경우 발생할 수 있는 충돌 방지**

```txt
로컬 PC
│
├── Project A
│   └── .venv
│       ├── Python 3.12
│       └── Django 5.2
│
└── Project B
    └── .venv
        ├── Python 3.11
        └── Django 4.2
```
**각 가상 환경은 독립적으로 패키지를 관리**하므로 프로젝트 A에서 Django를 업데이트 하더라도 프로젝트 B에는 영향을 주지 않음

**2. 프로젝트별 의존성 관리**

프로젝트 실행에 필요한 외부 라이브러리와 버전을 독립적으로 관리

또한 `requirements.txt` 파일을 통해 **필요한 패키지 목록을 기록하고 다른 개발자와 공유 가능**

**3. 시스템 Python 환경 보호**

프로젝트에서 사용하는 패키지를 시스템 전역에 직접 설치하지 않고 별도의 가상 환경에 설치하므로 **시스템 Python 환경을 불필요하게 변경하지 않음**

<br>

### 가상 환경 생성 및 활성화 

**1. 가상 환경 생성**
```bash
python -m venv venv # 또는 .venv

# macOS 명령어
python3 -m venv venv

# 특정 Python 버전 지정 가상 환경 생성 (3.9 버전 가상 환경 설정)
python3.9 -m venv venv
```
|명령어|설명|
|---|---|
|`python`|가상환경 생성에 사용할 Python 실행|
|`-m`|Python 모듈을 실행하는 옵션|
|`venv` (첫 번째)|Python 표준 라이브러리의 가상환경 생성 모듈|
|`venv` 또는 `.venv` (두 번째)|생성할 가상환경 디렉터리 이름|

**2. 가상 환경 활성화**
```bash
source venv/Script/activate

# macOS / Linux
source venv/bin/activate
```
가상 환경 실행 시 일반적으로 터미널 앞에 `(venv)` 또는 `((venv))` 표시

**3. 가상 환경 종료**
```bash
deactivate
```
가상 환경이 종료되면서, 다시 Python Global 환경으로 돌아옴

<br>

### Django 학습에서 가상 환경을 사용하는 이유

현재 단계에서는 Python과 Django 중심으로 프로젝트를 구성하고 SQLite 를 기본 데이터베이스로 사용

따라서 **별도의 데이터베이스 서버나 여러 서비스를 컨테이너로 구성할 필요 없음**

현재 기준 가상 환경만으로 요구사항 충족 가능

- [x] Django 프로젝트별 Python 및 라이브러리 관리
- [x] 프로젝트 간 패키지 버전 충돌 방지
- [x] `requirements.txt` 를 통한 의존성 관리
- [x] 별도의 컨테이너 설정 없이 간편한 개발 및 실행

<br>

### 가상 환경 주의사항 및 권장사항
**1. 가상 환경 디렉터리는 Git에 포함하지 않기**

가상환경 디렉터리에는 Python 실행 파일, 설치된 패키지, 환경 설정 등이 포함

이러한 파일은 용량이 크고 운영체제나 Python 설치 경로에 영향을 받기 때문에 Git으로 공유하는 것은 권장하지 않음

`.gitignore` 에 가상 환경 디렉터리 등록 -> `requirements.txt` 를 Git에 포함하여 필요한 패키지 목록 공유

**2. 프로젝트마다 별도의 가상 환경 사용**

여러 프로젝트가 하나의 가상환경을 공유하면 패키지 버전 충돌 발생 가능성 존재 (= 가상 환경을 사용하는 목적성 상실)

**3. Python 버전과 패키지 버전 구분**

```bash
# Python 3.12를 기반으로 가상 환경 생성
python3.12 -m venv venv

# 가상 환경 활성화
source venv/Script/venv

# Django 5.2 설치
pip install django==5.2
```
가상환경을 생성했다고 해서 Python 자체가 최신 버전으로 업데이트 되는 것이 아님

Python 버전을 변경해야 한다면 일반적으로 **원하는 버전으로 새로운 가상 환경 생성**이 안전

**4. `requirements.txt` 최신 상태 유지**

프로젝트 개발 중 새로운 패키지를 설치하거나 기존 패키지 버전을 변경했다면 의존성 목록도 갱신
```bash
pip freeze > requirements.txt
```

**5. 가상 환경 디렉터리를 이동하거나 복사 금지**

가상환경 내부에는 생성 당시의 Python 실행 경로 등이 기록될 수 있음

따라서 가상환경 디렉터리를 다른 PC로 복사하거나 프로젝트 경로를 이동하면 정상적으로 동작하지 않을 수 있음

**새로운 위치에서 가상환경을 새롭게 생성하고 패키지를 재설치 권장**

**6. 가상 환경에 "들어가고 나가는" 개념이 아닌 "On/Off" 개념**

가상 환경은 현재 터미널 환경에서만 영향을 끼침 

새 터미널 창을 열면 다시 활성화

<br>

### Python 가상 환경과 Docker Compose의 차이

두 기술은 모두 프로젝트별로 독립적인 환경을 구성하는 데 활용할 수 있지만, 목적과 **관리 범위**에 차이 존재

|구분|Python 가상 환경(`venv`)|Docker Compose|
|---|---|---|
|주요 목적|Python 실행 환경 및 패키지 분리|여러 Docker 컨테이너 관리|
|Python 버전|시스템 Python 환경 기반|컨테이너 이미지로 버전 지정|
|라이브러리 관리|프로젝트별 독립 관리|컨테이너별 독립 관리|
|시스템 의존성|별도 격리하지 않음|Docker 컨테이너를 통해 격리 가능|
|데이터베이스|별도 실행 및 관리|DB 컨테이너 함께 관리 가능|
|설정 및 실행|비교적 간단|추가 설정 필요|
|주요 활용|Python 프로젝트 개발 및 학습|다중 서비스 개발 환경 구성|

<br>

### 가상 환경과 Docker Compose의 선택 기준

|개발 상황|적합한 기술|
|---|---|
|Python 기본 학습|`venv`|
|Django 기본 학습 및 SQLite 사용|`venv`|
|Django + PostgreSQL 개발|`venv` + Docker 또는 Docker Compose|
|Django + PostgreSQL + Redis 등 여러 서비스|Docker Compose|
|컨테이너 기반 실행 환경 재현|Docker/Docker Compose|

<br>
<hr>
<br>

## 7. 의존성 패키지
Dependency Package란 **프로그램이나 프로젝트가 정상적으로 동작하기 위해 필요로 하는 외부 패키지들 의미**

### 의존성 패키지가 필요한 이유
- **개발 효율성** : 이미 구현된 기능을 재사용할 수 있음
- **유지보수** : 검증된 패키지를 활용하고 업데이트 할 수 있음
- **기능 확장** : 필요한 기능을 외부 패키지로 추가할 수 있음

예시로 Django에서 이미 제공하는 URL 라우팅, ORM, 인증 기능 등을 직접 처음부터 구현할 필요가 없는 것과 동일한 원리

### 직접 의존성과 간접 의존성

|구분|설명|
|---|---|
|직접 의존성|개발자가 프로젝트에서 사용하기 위해 직접 지정한 패키지|
|간접 의존성|직접 의존하는 패키지가 내부적으로 필요로 하는 다른 패키지|

[직접 의존성 & 간접 의존성](./images/03_직접%20의존성과%20간접%20의존성.png)

### 의존성 패키지 관리
Python에서는 `pip`와 `requirements.txt` 를 사용해 의존성 패키지를 관리하는 경우가 많음

가상 환경 활성화 상태 기준:

**1. 패키지 설치**
```bash
pip install django
```
- Django 패키지를 현재 가상 환경에 설치
- Django가 필요로 하는 간접 의존성 패키지도 함께 설치
- 다른 프로젝트의 가상 환경에는 영향을 주지 않음

**2. 설치된 패키지 확인**
```bash
pip list
```
- 현재 가상 환경에 설치된 모든 패키지와 버전을 확인 가능
- [예시]

**3. 의존성 패키지 목록 저장**
```bash
pip freeze > requirements.txt
```
- 현재 가상 환경에 설치된 패키지 목록과 버전을 `requirements.txt` 파일에 기록

**4. 의존성 패키지 일괄 설치**
```bash
pip install -r requirements.txt
```
- GitHub에서 다른 개발자의 프로젝트를 가져왔을 때
- 새로운 PC에서 기존 프로젝트의 개발 환경을 구성할 때
- 협업 중 동일한 의존성 패키지 버전을 설치해야 할 때

<br>
<hr>
<br>

## 8. Django 프로젝트

Django 프로젝트 생성 및 서버 실행 과정

가상 환경 설치 및 활성화 후 진행:
**1. Django 가상 환경에 설치**
```bash
pip install django
```

**2. Django 프로젝트 생성**
```bash
django-admin startproject firtpjt .
```
[프로젝트 생성 결과](./images/04_프로젝트%20생성%20결과.png)

**3. 서버 실행**
```bash
python manage.py runserver
```
[서버 실행 명령어 결과](./images/05_서버%20실행%20명령어%20결과%20터미널.png) &nbsp; | &nbsp; [서버 실행 후 브라우저 요청 결과](./images/06_서버%20실행%20후%20브라우저%20요청%20결과.png)

<br>
<hr>
<br>

## 9. Django Design Pattern

### Design Pattern (디자인 패턴)
소프트웨어 개발 과정에서 반복적으로 발생하는 설계 문제를 해결하기 위해 정리된 재사용 가능한 설계 방법

**개발자들이 비슷한 문제를 여러 번 해결하면서 발견한 효율적인 코드 구조와 설계 방법**

|목적|설명|
|---|---|
|유지보수성|기능별로 코드를 분리하여 수정하기 편리함|
|재사용성|비슷한 문제에 검증된 설계 방법을 활용할 수 있음|
|확장성|새로운 기능을 추가하거나 변경하기 쉬움|
|협업 효율성|개발자들이 공통된 설계 구조를 이해하고 작업할 수 있음|

### Django Design Pattern
Django는 웹 애플리케이션을 개발할 때 **[MTV](./images/07_Django%20MTV%20디자인패턴.png)**(Model-Template-View) 패턴 사용

**MTV 패턴의 구성 요소**

|구성 요소|역할|Django 파일|
|---|---|---|
|`Model`|데이터 구조 정의 및 데이터베이스와 상호작용|`models.py`|
|`Template`|사용자에게 보여줄 화면 구성|`*.html`|
|`View`|요청을 처리하고 필요한 데이터를 준비하여 응답 생성|`views.py`|

**1. Model**

Model은 애플리케이션에서 사용하는 데이터의 구조를 정의하고, 데이터베이스와 상호작용하는 역할 담당

Django에서는 ORM을 통해 Python 코드로 데이터베이스 조작 가능

```python
# model 클래스 예시

from django.db import models

class Article(models.Model):
    title = CharField(max_length=10)
    content = models.TextField()
```

해당 모델(클래스) 을(를) 기반으로 데이터베이스 테이블을 생성하고 데이터를 저장하거나 조회 가능

**2. Template**

Template은 사용자에게 보여줄 화면의 구조와 표현을 담당

HTML과 Django Template Language(DTL)를 사용하여 동적인 화면 구성 가능

View에서 전달받은 데이터를 HTML에 표시하는 역할

**3. View**

View는 클라이언트의 요청(Requests)을 받아 필요한 작업을 수행하고 HTTP 응답(Response)을 생성하는 역할 담당

```python
# view 예시

from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)
```

### MVC 패턴과 Django MTV 패턴 비교
웹 개발에서 자주 등장하는 설계 패턴으로 MVC(Model-View-Controller) 존재

Django의 MTV는 MVC와 개념적으로 유사하지만, 구성 요소의 이름과 역할 구분이 다름

|MVC 패턴|Django MTV 패턴|역할|
|---|---|---|
|Model|Model|데이터 관리|
|View|Template|화면 표시|
|Controller|View|요청 처리 및 응답 생성|

<br>
<hr>
<br>

## 10. 프로젝트와 앱

Django는 웹 서비스를 개발할 때 **Project(프로젝트)** 와 **App(앱)** 이라는 두 가지 구성 단위를 사용

프로젝트와 앱은 서로 역할이 다르며, 각각 생성했을 때 만들어지는 기본 파일들도 서로 다른 목적을 가지고 있다.

### Django Project 란?

Django Project는 **하나의 웹 서비스 전체를 구성하고 관리하는 최상단 단위**

프로젝트는 웹 서비스에 필요한 **공통 설정을 관리**하고, **여러 앱**이 하나의 서비스로 동작할 수 있도록 **연결**

#### 주요 역할

- 프로젝트 설정 관리 : 데이터베이스, 언어, 시간대, 보안 등 공통 설정
- 앱 관리 : 프로젝트에서 사용할 Django 앱 등록
- 최상위 URL 라우팅 : 클라이언트 요청을 적절한 View 또는 앱의 URL 설정으로 연결
- 미들웨어 관리 : 요청과 응답을 처리하는 공통 기능 설정
- 서버 연동 : WSGI 및 ASGI를 통한 서버 연결

#### 프로젝트 생성

[프로젝트 생성 방법](#8-django-프로젝트) &nbsp; | &nbsp; [프로젝트 디렉토리 구조](./images/08_Django%20프로젝트%20디렉토리%20구조.png)

**1. `manage.py`**

Django 프로젝트를 관리하기 위한 **명령어 실행 파일.**

개발자는 `manage.py` 를 통해 서버 실행, 마이그레이션, 앱 생성 등 다양한 작업 수행

|명령어|역할|
|---|---|
|`runserver`|개발 서버 실행|
|`startapp`|새로운 앱 생성|
|`makemigrations`|모델 변경사항을 마이그레이션 파일로 생성|
|`migrate`|마이그레이션 적용|
|`createsuperuser`|관리자 계정 생성|
|`shell`|Django 환경이 설정된 Python 셀 실행|
|`check`|프로젝트 설정 및 구성 검사|

<br>

**2. `init.py`**

**해당 디렉터리가 Python 패키지로 사용되도록 하는 파일**

`__init__.py` 는 패키지를 초기화할 때 실행되는 코드도 작성할 수 있지만, Django 프로젝트에서는 일반적으로 비어 있는 상태 유지

<br>

**3. `settings.py`**

**Django 프로젝트 전체에 적용되는 설정을 관리하는 파일**

가장 중요한 설정 파일 중 하나

**대표적인 설정**


- `INSTALLED_APPS` - 앱등록
    - [프로젝트 생성 시 자동 생성 앱 & 생성한 앱 등록](./images/09_settings.py_1.png) | 현재는 별도 생성 앱 없이 기본 제공 앱들만 존재
    - `django.contrib.admin` : 관리자 페이지
    - `django.contrib.auth` : 사용자 인증 및 권한 관리
    - `django.contrib.contenttypes` : 모델 타입 정보 관리
    - `django.contrib.sessions` : 세션 관리
    - `django.contrib.messages` : 일회성 메시지 관리
    - `django.contrib.staticfiles` : 정적 파일 관리

<br>

- `DATABASES` - 데이터베이스 설정
    - [데이터베이스에 관한 설정](./images/10_settings.py_2.png)
    - Django가 사용할 **데이터베이스 연결 정보 정의** (기본적으로 SQLite가 설정)

<br>

- `TEMPLATES` - 템플릿 설정
    - [HTML 템플릿 조회/처리 설정](./images/11_settings.py_3.png)
    - `BACKEND` : 사용할 템플릿 엔진
    - `DIRS` : 프로젝트 수준의 추가 템플릿 검색 경로
    - `APP_DIRS` : 설치된 앱 내부 `templates` 디렉터리 검색 여부
    - `OPTIONS` : 템플릿 엔진의 추가 설정

<br>

- `MIDDLEWARE` - 미들웨어 설정
    - [미들웨어에 대한 설정](./images/12_settings.py_4.png)
    - 미들웨어는 요청이 View에 도달하기 전이나 응답이 클라이언트로 전달되기 전후에 공통 처리를 수행하는 구성 요소
    - **HTTP 요청(Request)과 응답(Response)을 처리하는 과정에서 공통적인 작업을 수행**하는 구성요소
    - [미들웨어 동작과정](./images/13_middleware%20동작.png)

<br>

그 외 주요 설정

|설정|역할|
|---|---|
|`SECRET_KEY`|암호화 서명 등에 사용하는 비밀키|
|`DEBUG`|디버그 모드 활성화 여부|
|`ALLOWED_HOST`|허용할 요청 호스트|
|`ROOT_URLCONF`|최상위 URL 설정 모듈|
|`LAGUAGE_CODE`|기본 언어|
|`TIME_ZONE`|기본 시간대|
|`STATIC_URL`|정적 파일 URL 설정|
|`DEFAULT_AUTO_FIELD`|기본 자동 생성 기본키 필드 유형|

<br>

**4. `urls.py`**

클라이언트가 **요청한 URL을 적절한 View에 연결**하는 **URL 라우팅 설정 파일**

프로젝트의 `urls.py` 는 일반적으로 최상위 URL 라우팅 담당.

```python
from django.contrib import admin
from django.urls import path, include

urlspatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

<br>

**5. `wsgi.py`**

WSGI(Web Server Gateway Interface) 기반 서버와 Django 애플리케이션을 연결하기 위한 진입점

기본적으로 **동기 호출 모델을 기반**

<br>

**6. `asgi.py`**

ASGI(Asynchronous Server Gateway Interface) 기반 서버와 Django 애플리케이션을 연결하기 위한 진입점

**ASGI는 비동기 처리도 지원하는 인터페이스**

<br>
<br>

### Django App 이란?

Django App은 프로젝트 내부에서 **특정 기능을 구현하고 관리하는 구성 단위**

프로젝트가 웹 서비스 전체를 담당한다면, **앱**은 게시글 관리나 회원 관리처럼 **특정 기능에 집중**

[Project와 App의 관계 예시](./images/14_Django%20Project%20와%20App%20관계%20예시.png)

#### 앱 생성

```bash
python manage.py startapp articles
```
[앱 디렉터리 구조](./images/15_생성된%20app%20디렉터리%20구조.png)

앱 생성 직후에는 일반적으로 `urls.py`, `templates/` 디렉터리 등이 생성되지 않음 -> **필요한 경우 직접 추가**

[project `settings.py` 파일에 앱 등록](./images/16_생성된%20app등록.png)



<br>

**1. `models.py`**

**데이터베이스에서 관리할 데이터의 구조를 Python 클래스로 정의하는 파일**

Django의 ORM(Object-Relational Mapping)을 통해 **Python 코드로 데이터베이스 작업을 수행할 수 있도록 함**

이후 추가적으로 학습 예정

<br>

**2. `views.py`**

**클라이언트의 HTTP 요청을 처리하고 HTTP 응답을 생성하는 로직을 작성하는 파일**

Django의 View는 요청을 전달받아 필요한 데이터를 조회하거나 처리하고, 그 결과를 응답으로 반환

View는 반드시 HTML을 반환하는 것이 아닌 **JSON이나 리다이렉트 응답 등을 반환할 수도 있음**

<br>

**3. `admin.py`**

Django **관리자 페이지에서 모델을 관리할 수 있도록 등록하고 설정**하는 파일

관리자 페이지에 로그인하려면 적절한 권한을 가진 계정 필요 

<br>

**4. `apps.py`**

Django **앱의 설정 정보를 정의하는 파일**

<br>

**5. `tests.py`**

앱의 기능이 정상적으로 동작하는지 확인하는 **테스트 코드를 작성하는 파일**

프로젝트가 커지면 `tests/` 패키지를 만들어 테스트 코드를 나누기도 함
```bash
# 테스트 실행 명령어
paython manage.py test
```

<br>

**6. `migrations/디렉터리`**

**모델 변경사항을 데이터베이스 스키마에 반영하기 위한 마이그레이션 파일들을 관리하는 디렉터리**

이후 추가적을 학습 예정

<br>

**7. `init.py`**

앱 디렉터리의 `__init__.py` 또한 Python 패키지와 관련된 파일

앱의 모듈을 Python에서 import할 수 있는 패키지 구조로 구성

<br>
<br>

### Project 와 App 역할 비교

|구분|Project|App|
|---|---|---|
|관리 범위|웹 서비스 전체|특정 기능|
|설정 관리|`settings.py`|`apps.py`|
|URL 관리|최상위 `urls.py`|별도 생성한 `urls.py`|
|데이터 모델|보통 앱에서 관리|`models.py`|
|요청 처리|앱의 View로 연결|`views.py`|
|데이터베이스 변경 이력|프로젝트 전체에서 적용 관리|`migrations/`|
|테스트|프로젝트 단위 테스트도 가능|`tests.py`|
|재사용성|전체 서비스 단위|앱 단위 재사용 가능|

<br>
<br>

### 전체 정리

#### Django Project

웹 서비스 전체를 구성하고 관리하는 단위. `settings.py` 를 통해 공통 설정을 관리하고, 최상위 `urls.py` 를 통해 URL 라우팅을 구성

<br>

#### Django App

프로젝트에서 특정 기능을 구현하는 단위. `models.py` 로 데이터 구조를 정의하고, `views.py` 로 요청을 처리하며, `admin.py`, `tests.py`, `migrations/` 등을 통해 기능 관리

<br>

#### Project 와 App 관계

Django는 하나의 프로젝트 안에 여러 앱을 구성할 수 있고, 프로젝트는 전체 설정과 연결을 담당하며 각 앱은 맡은 기능을 구현한다.

<br>
<hr>
<br>

## 11. 요청과 응답

- 요청 : HTTP Request
- 응답 : HTTP Response

**Django는 클라이언트가 요청을 처리하고, 그 결과를 응답으로 반환하는 웹 프레임워크**

### HTTP 요청과 응답이란?

|구분|HTTP Request|HTTP Response|
|---|---|---|
|의미|클라이언트가 서버에 보내는 요청|서버가 클라이언트에게 반환하는 응답|
|방향|Client -> Server|Server -> Client|
|목적|데이터 조회, 생성, 수정, 삭제 등 요청|요청 처리 결과 전달|
|주요 정보|HTTP Method, URL, Header, Body|Status Code, Header, Body|
|Django 객체|`HttpReqeust`|`HttpResponse`|

### Django의 HTTP 요청 - `HttpRequest`

Django는 클라이언트로부터 **HTTP 요청을 받으면** 해당 **요청 정보를 담은 `HttpRequest` 객체 생성**

#### `HttpRequest` 주요 속성

|속성|설명|
|---|---|
|`request.method`|HTTP 요청 메서드 (GET, POST 등)|
|`request.GET`|URL 쿼리 문자열의 데이터|
|`request.POST`|폼 형식으로 전송된 요청 본문 데이터|
|`request.FIELS`|업로드된 파일 데이터|
|`request.path`|요청 URL의 경로|
|`request.headers`|HTTP 요청 헤더|
|`request.COOKIES`|클라이언트가 보낸 쿠키|
|`request.user`|현재 사용자 정보(인증 미들웨어 사용 시)

### Django의 HTTP 응답 - `HttpResponse`

Django의 View는 요청을 처리한 후 `HttpResponse` 객체 또는 그 하위 클래스의 객체 반환

#### `HttpResponse` 주요 속성

|속성|설명|
|---|---|
|`response.status_code`|HTTP 응답 상태 코드|
|`response.content`|응답 본문 데이터(bytes)|
|`response.headers`|HTTP 응답 헤더|
|`response.charset`|응답 문자 인코딩|

**1. HttpResponse 직접 반환**

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Django!', status=200)
```

```HTTP
# 클라이언트가 받는 응답 모습
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

Hello Django!
```
**2. `render()`를 통한 HTML 응답**
```python
from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')
```

- 두 방식의 차이점은 `HttpResponse()` 는 응답 내용을 직접 지정하고, `render()` 는 템플릿을 이용해 HTML 응답을 생성
- [HTTP Request - HTTP Response 동작 과정](./images/17_Django%20요청%20-%20응답%20동작%20과정.png)

### 요청 - 응답 코드 작성 순서

**1. 프로젝트 생성 및 앱 생성&등록 과정 생략**

**2. 프로젝트 `urls.py` -- URL Routing**

```python
from django.contrib import admin
from django.urls import path
from articles import views # articles 앱 패키지의 views 모듈 추가

urlspatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
]
```
- 클라이언트의 HTTP 요청 URL과 실행할 View 함수 연결
- `articles` 앱의 `views` 모듈 import
- `/articles/` 경로로 요청이 들어오면 `views.index` 함수 실행
- **목적 : URL Routing을 통해 요청을 처리할 View 함수를 지정하는 단계** 

**3. 앱 `views.py` -- View 함수 작성**

```python
from django.shortcuts import render

def index(request):

    return render(request, 'articles/index.html')
```
- Django가 생성한 `HttpRequest` 객체를 `request` 매개변수로 전달받음
- `render()` 함수를 호출하여 HTML 템플릿 렌더링
- 랜더링된 HTML을 담은 `HttpResponse` 객체 반환

>**`render()` 함수**
>`render()` 는 Django의 View 함수에서 HTML 템플릿에 데이터를 적용하고, 완성된 HTML을 담은 `HttpResponse` 객체를 반환하는 함수
>
>즉, HTML 파일과 View에서 전달한 데이터를 결합하여 클라이언트에게 반환할 HTTP 응답을 생성하는 역할 수행
>
>1. 지정한 HTML 템플릿 탐색
>2. 필요시 HTML 템플릿에 전달할 데이터 적용
>3. 완성된 HTML 문서 생성
>4. 생성한 HTML을 `HttpResponse` 객체에 담아 반환
>
>`render()` 함수 기본 구조
>`render(request, template_name, context)`

**4. HTML Template -- 템플릿 작성**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Article 앱 인덱스 페이지</title>
</head>
<body>
    <h1>Hello Django!</h1>
</body>
</html>
```
- 클라이언트에게 전달할 HTML 문서 정의
