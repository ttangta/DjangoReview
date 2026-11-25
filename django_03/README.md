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
