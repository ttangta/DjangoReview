## 1. 학습 목표 요약

![학습 목표 요약](./images/01_Djngo%20Model%20Intro.png)

<br>
<hr>
<br>

## 2. Model

**Django의 Model은 애플리케이션에서 사용할 데이터의 구조와 동작을 정의하는 구성 요소**

예를 들어 게시판에서 **게시글이라는 데이터를 관리**하려면 제목, 내용, 게시글과 관련된 동작을 정의하는 것이 Model의 역할

Django의 MTV 디자인 패턴에서 M(Model)에 해당하며, **일반적으로 데이터베이스(DB)의 테이블과 연결**

<br>
<hr>
<br>

## 3. Model Class

**Model Class**는 Django의 **Model을 Python 클래스로 구현한 것**

특정 앱의 `models.py` 파일에서  `models.Model` 클래스를 상속받아 작성

```python
# articles/models.py
from django.db import models

class Article(model.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

[Model Class 와 DB 관계](./images/02_Model%20and%20DB.png)

- Model Class의 **클래스 변수명** : 테이블의 각 필드(열) 이름
- Model Field : 데이터베이스 테이블의 열을 나타내는 구성 요소, "데이터 유형"과 "제약 조건" 정의

<br>
<hr>
<br>

## 4. Model Field

**Model Field**는 **Model 클래스에서 개별 데이터 항목의 자료형과 속성을 정의**하는 요소

일반적으로 **Model Field 하나는 DB 테이블의 열(Column) 하나와 대응**

```python
# articles/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    views = models.IntegerField(default=0)
```

|필드 이름|Field 종류|관리하는 데이터|
|---|---|---|
|`title`|`CharField`|게시글 제목|
|`content`|`TextField`|게시글 내용|
|`views`|`IntegerField`|조회수|

<br>

### Model Field 작성 구조
![Model Field 작성 구조](./images/03_Model%20Field%20작성%20구조.png)

**1. 필드 이름 - `title`**

Model에서 해당 데이터 항목을 식별하는 이름. 기본적으로 DB 테이블 컬럼명도 `title`이 됨

**2. 필드 종류 -- `models.CharField`**

어떤 종류의 데이터를 관리할지 정의하는 Field 클래스. 

**3. 필드 옵션 -- `max_length=100`**

Field의 세부 속성을 설정하는 인자. 해당 예시에서는 문자열의 최대 길이를 100을 지정

- `title` 이라는 문자열 필드를 정의하고 최대 길이는 100으로 설정

<br>

### Model Field 주요 역할

**1. 데이터의 자료형 정의**

필드 종류에 따라 Django가 값을 **어떤 Python 자료형으로 다룰지 결정**

<br>

**2. 데이터베이스 컬럼의 구조 정의**

일반적인 Model Field는 Migration을 통해 **DB 테이블의 컬럼을 생성하거나 변경할 때 필요한 정보 제공**

Model Field를 통해 **기본 키를 정의하지 않으면 Django가 `id` 라는 기본 키를 자동을 추가**

<br>

**3. 데이터 유효성 검사에 필요한 정보 제공**

Model Field는 값이 올바른지 검사할 때 사용할 규칙도 제공 

다만 **Field에 규칙을 정의하는 것과 실제로 유효성 검사를 실행하는 것은 별개**

Model 인스턴스의 `save()`는 `full_clean()`을 자동으로 호출하지 않음. 또한 **모든 Field 옵션이 DB 테이블 컬럼에 제약조건으로 만들어지는 것은 아님**

<br>

### Field Types

Field Type은 **필드에 저장할 데이터의 종류를 정의하는 클래스.** Django는 이를 바탕으로 DB 테이블의 열(Column)의 자료형, 기본적인 유효성 검사, ModelForm에서 사용할 기본 입력 필드 등을 결정

주의 : **Field Type이 제공하는 검사와 DB가 강제하는 규칙은 같지 않다.** 예를 들어 `EmailField` 는 Django의 유효성 검사 과정에서 이메일 형식을 확인하지만, DB가 직접 입력되는 모든 값의 이메일 형식을 검사한다는 뜻은 아님

**주요 Field Types**

|Field|용도|예시|
|---|---|---|
|`CharField`|길이가 제한된 문자열|제목, 이름|
|`TextField`|긴 문자열|게시글 본문|
|`IntegerField`|정수|조회수|
|`DecimalField`|정해진 자릿수의 십진수|금액|
|`BooleanField`|참 또는 거짓|공개 여부|
|`DateField`|날짜|생년월일|
|`DateTiemField`|날짜와 시간|작성일|
|`ForeignKey`|다른 Model과의 다대일 관계|게시글 작성자|

<br>

### Field Options 

**Field Options는 Field Type에 전달하는 필드의 세부 동작을 설정하는 인자.** 데이터의 허용 범위, 필수 입력 여부, 기본값, DB 제약조건 등을 지정가능

```python
# 특정 모델 클래스 내부 클래스 변수(테이블 열) 옵션 지정
title = models.CharField(
    max_length=100,
    blank=False,
    null=False,
    unique=True,
)
```

해당 필드는 문자열을 관리하며, 최대 길이는 100자이고, Django 유효성 검사에서 빈 값을 허용하지 않으며, DB에서는 `NULL` 과 중복 값을 허용하지 않도록 정의됨

**주요 Field Options**

|Option|설명|
|---|---|
|`max_length`|문자열의 최대 길이|
|`blank`|**유효성 검사에서** 빈 값 허용 여부|
|`null`|DB 컬럼의 `NULL` 허용 여부|
|`default`|값을 지정하지 않았을 때 사용할 기본값|
|`unique`|DB에서 값의 중복을 제한|
|`primary_key`|기본 키(PK)로 지정|
|`choices`|유효성 검사 등에서 허용할 선택지 지정|
|`validators`|추가 유효성 검사 함수 지정|
|`db_index`|DB 인덱스 생성 지정|
|`verbose_name`|사람이 읽기 좋은 필드 이름|

<br>

**`null` 과 `blank`**

두 옵션은 모두 기본값이 `False` 이지만, 적용되는 위치가 다름

|구분|`null=True`|`blank=True`|
|---|---|---|
|적용 대상|DB|Django 유효성 검사|
|의미|`NULL` 저장 허용|빈 값 입력 허용|
|대표 사례|선택적인 날짜|선택적인 자기소개|

```python
class Profile(models.Model):
    bio = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)
```
`bio` 는 작성하지 않으면 보통 빈 문자열 `""` 로 저장. 반면 `birthday`는 날짜가 없다는 것을 DB에 `NULL`로 저장할 수 있게 설정

일반적인 문자열 필드에는 `null=True` 보다 `blank=True`를 사용하는 것이 권장
- 값이 없는 상태를 `""`와 `NULL` 두 가지로 나누지 않기 위해

<br>

### Field Type 과 Option이 실제로 적용되는 위치

```python
class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

|설정|주요 역할|
|---|---|
|`CharField`|문자열에 맞는 DB 열(Column) 유형과 Django 필드 동작 결정|
|`max_length=100`|Django의 길이 검사 및 DB별 컬럼 정의에 반영|
|`unique=True`|DB에 고유성 제약조건 생성|
|`blank=True`|Django 유효성 검사에서 빈 내용 허용|
|`auto_now_add=True`|Django ORM으로 처음 저장할 때 현재 시각 설정|

모델을 정의했다고 모든 규칙이 DB에 자동으로 적용되는 것 아님

스키마 변경은 Migration을 생성하고 적용해야 DB에 반영됨

`save()`, `objects.create()` 는 모델의 `full_clean()`을 자동 호출하지 않으므로, Django 유효성 검사가 필요한 경우 별도로 수행해야 함
- **SQL로 DB를 직접 조작하면 Django의 유효성 검사 과정을 거치지 않음**

<br>
<hr>
<br>

## 5. Migrations (마이그레이션)

Django의 **Migration**은 **Model의 변경 사항을 기록**하고, 그 **변경 사항을 DB 구조에 반영할 수 있도록 관리하는 기능**

**Model의 변경사항**은 `models.py` 에 정의한 **Model Class의 변경사항 의미**
- Model의 변경사항은 필드 생성, 수정, 삭제등과 **새로운 Model Class 작성 또한 변경사항에 포함**

```python
# articles/models.py
# Article Model Class 작성이라는 변경사항 발생

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

**`models.py` 에 클래스를 작성했다고 해서 DB 테이블이 즉시 생성되는 것 아님** &nbsp; | &nbsp; [Migrations 전체 흐름](./images/04_Migrations%20전체%20과정.png)

- Model은 원하는 데이터 구조 정의
- Migration은 그 구조가 어떻게 변경되어 왔는지 관리

<br>

### Migration 필요성

최초 작성부터 완벽한 Model 작성은 어려움. 요구사항 변경 등 여러가지 상황에 따라 Model의 구조가 변경될 수 있기 때문

Model의 변경이 필요할 때 기존 DB 제거하고 새로 만드는 방식은 적절하지 않음. 

**기존 데이터를 유지하면서 필요한 구조만 변경해야 함**

Migration은 이러한 **변경을 작업 단위로 기록하고 순서대로 적용**할 수 있도록 도와줌

또한 협업 시 동일한 Migration 파일을 적용하면 각자 DB 구조를 일관되게 맞출 수 있음

단, **Migration**이 모든 변경에서 **데이터를 자동으로 보존해 주는 것은 아님.** (필드를 삭제하면 해당 컬럼의 데이터 사라질 수 있음)

<br>

### Migration 핵심 구성 요소

|구성 요소|역할|
|---|---|
|Model|애플리케이션에서 사용할 데이터 구조 정의|
|Migration 파일|Model 변경 작업과 의존 관계 기록|
|`makemigrations`|변경 사항을 감지해 Migration 파일 생성|
|`migrate`|Migration 작업을 실제 DB에 적용|

### Migrations 진행 과정

**1. Model 정의**

프로젝트 : 생성, URLconf 작성, articles 앱 등록, 추가 templates 경로 등 ... 과정 생략

앱 : 생성, App URLconf 작성, Namespace, Naming URL Pattern 과정 생략

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```
[모델 클래스 작성 실제 코드](./images/06_Model%20Class%20작성.png)

<br>

**2. Migration 파일 생성 -- `makemigrations`**

```bash
python manage.py makemigrations
```
해당 과정까지는 DB에 `Article` 테이블이 생성된 것은 아님

현재 Model 상태와 기존 Model 비교 **(Model Class 와 DB 테이블 직접 비교가 아님)**

[makemigrations 명령어 수행 결과](./images/07_Migration%20파일%20생성%20결과.png) &nbsp; | &nbsp; [추가된 Migration 파일 확인](./images/08_Migration%20추가%20확인.png) &nbsp; | &nbsp; [Migration 파일 상세](./images/09_Migration%20파일%20상세.png)

<br>

**3. DB 적용 -- `migrate`**

```bash
python manage.py migrate
```

[migrate 명령어 수행 결과](./images/10_Migrate%20명령어%20실행%20결과.png) &nbsp; | &nbsp; [DB에 생성된 table 확인](./images/11_Migrate로%20생성된%20테이블.png)

<br>

### Migration 경고 메시지

![Migration 진행 전 서버 실행 시 경고](./images/05_Django%20Server%20실행%20시%20경고.png)

프로젝트 실행 시 미적용 마이그레이션 파일이 있을 때 발생

- `python manage.py migrate` 진행 후 서버 실행 시 사라짐
- [Migration 진행 후 서버 실행](./images/12_Migrations%20진행%20후%20서버%20실행.png)

<br>
<hr>
<br>

## 6. 추가 Migrations

기존 **Migration에 기록된 Model의 상태가 변경**되었을 때, 그 **차이를 새로운 Migration 파일로 기록**하는 작업

새로운 Migration 파일을 만들어 변경 이력을 이어 나가는 방식

<br>

### 기록하는 Model의 변경사항

|Model 변경사항|대표적인 Migration 작업|
|---|---|
|새로운 Model Class 작성|`CreateModel`|
|기존 Model에 필드 추가|`AddField`|
|필드의 타입이나 옵션 변경|`AlterField`|
|필드 이름 변경|`RenameField`|
|필드 삭제|`RemoveField`|
|Model 삭제|`DeleteModel`|

<br>

### Article Model Field에 created_at, updated_at 필드 추가 상황

```python
# articles/models.py

from django.db import models

# 기존 Migration 적용 부분
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 새롭게 추가되는 필드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTiemField(auto_now=True)
```

[모델 클래스 필드 추가 실제 코드](./images/13_Model%20Class%20Field%20추가.png)

|추가된 필드|옵션|역할|
|---|---|---|
|`created_at`|`auto_now_add=True`|객체를 처음 저장할 때 현재 시각 자동 입력|
|`updated_at`|`auto_now=True`|객체를 `save()` 할 때 현재 시각 자동 입력|

추가된 두 필드 모두 `null` 을 별도로 지정하지 않았으므로, 기본적으로 `null=False`

즉, DB에서 `NULL` 을 허용하지 않음

`auto_now_add` 와 `auto_now` 는 **앞으로 객체를 저장할 때 동작**하는 옵션 -> 기존 게시글의 실제 작성일과 수정일을 알 수 없음

<br>

**`makemigrations` 실행 시 발생하는 질문**

기존에 존재하는 데이터들에 대한 해당 필드에 대한 값 요구

![추가 Migrations 예시 상황](./images/14_추가%20Migrations%20시%20발생%20상황%20예시.png)

`makemigrations` 는 실제 DB의 행의 개수가 아니라 **기존 Migration 상태와 현재 Model 상태를 비교**하기 때문에 **기존 데이터가 존재하지 않더라도 기본값에 대한 질문 수행**

![추가 Migrations 시 기본값 요구 프롬프트](/images/15_추가%20Migrations%20에%20대한%20Djnago%20기본값%20요구%20프롬프트.png)

<br>

**방법 1: 일회성 기본값 지정**

기존 게시글의 정확한 작성/수정 시각을 알 수 없고, **필드 추가 시점을 초기값으로 사용**해도 무관할 때 사용 가능

[기본값 질문 프롬프트 답변 예시](./images/16_기본값%20요구%20프롬프트%20답변.png) &nbsp; | &nbsp; [추가된 Migration 파일 확인](/images/17_추가된%20Migration%20파일.png) &nbsp; | &nbsp; [추가 Migration 파일 상세](./images/18_추가된%20Migration%20파일%20상세.png)

<br>

**방법 2: Model에 지속적인 `default` 지정하기**

```python
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

```

<br>

**방법 3: 기존 날짜를 정확히 복원한 뒤 `null=False` 적용**

기존 게시글의 실제 작성일과 수정일을 다른 기록에서 복원할 수 있다면, 모든 행에 현재 시각을 넣는 대시 단계적으로 진행

```python

# 1. 날짜가 없는 상태 임시 허용
created_at = models.DateTimeField(null=True)
updated_at = models.DateTimeField(null=True)

# 2. Migration 적용
# 데이터 Migration 등을 이용해 기존 행마다 올바른 시각 채움 이후, NULL이 남아있는지 확인
Article.objects.filter(created_at__isnull=True).exists()
Article.objects.filter(updated_at__isnull=True).exists()

# 두 결과가 모두 False인지 확인

# 3. 원하는 최종 모델로 변경
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

<br>
<hr>
<br>

## 7. Admin Site 

Django의 **Admin Site**는 **Model에 저장된 데이터를 관리**할 수 있도록 **Django가 기본 제공하는 관리자용 웹 인터페이스**

예를 들어 일반적으로 게시글을 관리하는 웹페이지를 만들려면 URL, View, Template, Form 등을 작성해야 함.
- **Admin Site**를 사용하면 **Model을 등록**하는 것만으로도 **관리자 화면에서 데이터 CRUD 기능 사용 가능**

![Admin Site](./images/19_Django%20Admin%20Site%20접속화면.png)

<br>

### Admin Sited 와 Model의 관계

![Admin Site - Model](./images/20_Admin%20Site%20와%20Model%20관계.png)

Admin Site는 등록된 Model의 정보를 이용해 화면 구성하고, Django ORM을 통해 DB의 데이터 조작

<br>

### Admin Site 사용 방법

**1. 관리자 계정 생성**

![superuser 생성](./images/21_superuser%20생성.png)

[superuser 생성 결과](./images/22_superuser%20생성%20결과.png)

<br>

**2. Model을 Admin Site에 등록**

```python
# articles/admin.py

from django.contrib import admin
from .models import Article

admin.site.register(Article)
```
[실제 Model 등록 코드](./images/23_Model%20Class%20Admin%20Site%20등록.png)

**Model을 정의했다고 해서 Admin Site에 자동으로 표시되는 것 아님** 

관리 화면에서 사용할 Model을 직접 등록해야 함


**3. 서버 실행 및 접속**

![Admin Site 예시](./images/24_Admin%20Site%20활용%20예시.gif)

[Admin Site를 통해 생성된 데이터 확인](/images/25_Admin%20Site를%20통해%20실제%20생성된%20데이터.png) &nbsp; | &nbsp; [Admin Site에서 Model Instance 표현 방법 설정](./images/26_Model%20Instance%20표현방법%20설정.png)

<br>
<hr>
<br>

## 8. DB 초기화

데이터베이스 초기화는 개발 과정에서 저장된 데이터나 DB 구조를 정리하여 원하는 시작 상태로 되돌리는 작업

다만 **초기화가 항상 DB 전체 삭제를 의미하는 것 아님.** 무엇을 남기고 무엇을 지울지에 따라 방법 상이

|구분|의미|
|---|---|
|데이터|게시글, 사용자 계정 등 테이블에 저장된 행|
|DB 스키마|테이블, 컬럼, 제약조건 등의 구조|
|Migration 이력|Model 구조가 어떻게 변경되었고 어떤 변경이 적용되었는지에 대한 기록|

- 게시글만 지우는 것과 `articles_article` 테이블 자체를 지우는 것은 전혀 다른 작업

<br>

### 목적에 따른 초기화 방법

|목적|방법|유지되는 것|
|---|---|---|
|특정 Model의 데이터만 삭제|ORM의 `delete()`|테이블 구조, Migration 이력|
|프로젝트의 데이터를 비우기|`flush`|테이블 구조, 적용된 Migration 이력|
|개발용 DB 새로 생성|DB 재생성 후 `migrate`|기존 Migration 파일|
|특정 Migration 이전 구조로 되돌리기|`migare 앱이름 대상`|대상 시점의 구조|

<br>

**1. 특정 Model 데이터만 삭제**

```bash
python manage.py shell
```

```python
from articles.models import Article

Article.objects.all().delate()
```

실행 후에는 데이터는 없지만 `articles_article` 테이블과 컬럼은 그대로 존재

관리자 계정도 별도로 삭제하지 않았다면 유지

일반적으로 데이터를 초기화 했다고 해서, PK의 값이 1로 초기화 되는 것은 아님

<br>

**2. `flush` 로 데이터 초기화**

```bash
python manage.py flush
```

프로젝트 테이블 구조는 유지하면서 데이터를 비움

`flush` 의 핵심은 Migration을 취소하지 않음

<br>

**3. SQLite DB 삭제 후 재생성**

개인 학습 프로젝트에서 DB 파일 자체를 새로 만들고 싶을 때 사용

`db.sqlite3` 삭제 후 `python manage.py migrate`

해당 방법은 DB에 존재하던 데이터와 적용 이력 모두 사라짐. 하지만 Migration 파일은 유지 (`makemigrations` 재실행 필요 없음)

<br>
<hr>
<br>

## 9. Migrations 관련

### Migrations 주요 명령어

`makemigrations` 와 `migate` 

|명령어|역할|실행 결과|
|---|---|---|
|`showmigrations`|Migration의 적용 상태 확인|[showmigration 명령어 결과](./images/27_showmigrations%20결과.png)|
|`sqlmigrate`|특정 Migration에 대응하는 SQL 확인|[sqlmigrate 명령어 결과](./images/28_sqlmigrate%20명령어%20결과.png)|

<br>

### 최초 `migrate` 시 출력 내용이 많은 이유

Django 프로젝트가 동작하기 위해 미리 작성되어 있는 기본 내장 app 들에 대한 Migration 파일들이 함께 migrate 되기 때문

<br>
<hr>
<br>

## 10. SQLite

