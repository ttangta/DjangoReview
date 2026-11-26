from django.db import models

# Create your models here.

# 1. articles 앱에서 Model Class 작성 -> (Model Class 작성이라는 변경사항 발생)
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    # 2. Migration 적용 후 추가된 Model Field (기본적으로 null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 3. sqlmigrate를 위한 임시 필드 추가
    views = models.IntegerField(default=0)

    # Admin Site에서 Aritlce 인스턴스 객체를 문자열로 표현하는 방법 
    # __str__() 는 Python Method 이므로, 해당 함수만 추가했을 경우 Migration 하지 않아도 됨
    def __str__(self):
        return self.title