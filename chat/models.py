from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    key = models.CharField(max_length=32)
    nickname = models.CharField(max_length=30, default='anonymous')
    def __str__(self):
        return f"Nickname: {self.nickname}, ID: {self.id}"

class Group(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return f"Group: {self.name}"

class Post(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content

    def dispatch(self):
        return {
            'id': self.id,
            'content': self.content,
            'date': self.date, 
            'group': self.group,
            'user': self.user.nickname
        }

