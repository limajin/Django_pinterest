from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    # reverse_lazy 주소를 역추적하는 건 같지만
    # 함수형 view에서는 바로 불러주면 되지만
    # 객체가 생성되고나서 따로 불러줘야해서 reverse_lazy
    # 성공했을 때 넘어가는 url
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

