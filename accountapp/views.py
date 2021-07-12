from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')
        # input 안에 POST안에 input_text

        new_hello_world = HelloWorld()
        # 새로운 객체 생성
        new_hello_world.text = temp
        new_hello_world.save()
        # 데이터베이스에 새로운 행 (반영)


        return render(request, 'accountapp/hello_world.html',
                      context={'new_hello_world': new_hello_world})
        # 객체를 보내줌

    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})
