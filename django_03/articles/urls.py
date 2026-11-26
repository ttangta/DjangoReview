from django.urls import path
from . import views

# Namespace 지정
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index')
]

