from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        # 어떤 유저가 정보를 요청하는지

        project = Project.objects.get(pk=kwargs['project_pk'])
        # 어떤 게시판?

        subscription = Subscription.objects.filter(user=user,
                                                  project=project)
        # 기존에 이페이지를 구독했는지

        if subscription.exists():
            subscription.delete()
        # 구독되어있으면 지워주고 없다면 만들어줌

        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': kwargs['project_pk']})