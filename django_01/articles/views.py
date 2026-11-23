from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # 모든 view 함수는 첫 번째 인자로 요청 객체(request)를 필수적으로 받음
    print(request)
    return render(request, 'articles/index.html')

# HttpResponse 직접 반환하는 view 함수
def useHttpResponseObject(request):
    return HttpResponse('HttpResponse 객체 직접 반환', status=200)