from django.shortcuts import render

# Create your views here.
def fake(request):
    return render(request, 'fake_naver/fake_naver.html')