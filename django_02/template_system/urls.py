"""
URL configuration for template_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dinners import views
from fake_naver import views as fake_views
from throw_catch import views as tc_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinners/', views.menu),
    path('fake/', fake_views.fake),
    path('throw/', tc_views.throw),
    path('catch/', tc_views.catch),
]
