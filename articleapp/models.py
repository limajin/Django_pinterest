from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    # 연결된 유저객체가 삭제 됐을 때 작성자 미상의 글로 남겨두겠다

    project = models.ForeignKey(Project,on_delete=models.SET_NULL,
                                related_name='article', null=True, blank=True)
    # 여기서 null = True는 디비상 널 트루임 실제 입력을 받지않아도는 아님

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    # 긴문자열 TextField

    created_at = models.DateField(auto_now_add=True, null=True)
    # 여기서 null = True는 디비상 널 트루임 실제 입력을 받지않아도는 아닌다.
    # 시간 정보 자동 입력되게

    like = models.IntegerField(default=0)