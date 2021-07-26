from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # on_delete 삭제 되었을 때 CASCADE 종속되어있는 것도 삭제
    # SET_NULL로 세팅하면 모르는 사람으로 설정되게
    # related_name는 target_user.profile 이런식으로 사용하기위해서 써주는 것

    image = models.ImageField(upload_to='profile/', null=True)
    # media 에서 profile이라는 폴더를 만들어서 저장하겠다 라는 경로를 지정함

    nickname = models.CharField(max_length=30, unique=True, null=True)
    # 모든 유저 사이에서 중복이 없게

    message = models.CharField(max_length=200, null=True)
