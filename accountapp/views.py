from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

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

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # accountapp 안에 있는 hello_world 라우트로 가라 (reverse -> 주소 역추적)
        # 마지막 요청을 get으로 redirect
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})
