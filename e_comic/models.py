from django.db import models
from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=128,null=False)
    email = models.EmailField(max_length=264,null=True,unique=True)
    age = models.PositiveSmallIntegerField(default=0)