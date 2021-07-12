from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')
        # input 안에 POST안에 input_text

        return render(request, 'accountapp/hello_world.html',
                      context={'text': temp})
        # 유저에게 입력받은 것을 그대로 출력

    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})
