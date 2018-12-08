from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class Account(AbstractUser):
    # Username = models.CharField(max_length=20)
    # Password = models.CharField(max_length=50)
    # cre_date = models.DateTimeField('date published', default=timezone.now())
    age = models.IntegerField(default=0)
    sex_choice = ((0, 'Nữ'), (1, 'Nam'))
    address = models.CharField(default='', max_length=50)
    sex = models.IntegerField(choices=sex_choice, default='1')
    phone = models.CharField(max_length=11)


class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    context = models.CharField(max_length=1000)
    time_creat = models.DateTimeField()

    def __str__(self):
        return str(self.context)


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cmt = models.CharField(max_length=500)

    def __str__(self):
        return str(self.user)


class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.likes)


