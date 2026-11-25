from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'throw_catch/throw.html')

def catch(request):
    # GET 요청 시 URL 경로에 포함된 데이터 가져오기
    message = request.GET.get('message')

    # 템플릿에 전달할 데이터 만들기 -> Context 구성
    context = {
        'message': message
    }

    return render(request, 'throw_catch/catch.html', context)