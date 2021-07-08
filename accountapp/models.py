from django.db import models

# Create your models here.


class HelloWorld(models.Model):
    # 클래스를 상속받아서 클래스 만듦


    text = models.CharField(max_length=255, null=False)
