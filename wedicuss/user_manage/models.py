from django.db import models
from django.contrib.auth.models import User
import hashlib
# Create your models here.
class User_group(models.Model):
    name = models.CharField(max_length = 20)
    permissions = models.IntegerField()

    def __unicode__(self):
        return self.name

class User_info(models.Model):
    name = models.CharField(max_length = 20)
    nickname = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.EmailField()
    state = models.IntegerField()
    coins = models.IntegerField()
    group =  models.ForeignKey(User_group)

    def __unicode__(self):
        return u"name:%s state:%d" \
        %(self.name,self.state)


class User_relation(models.Model):
    user_a = models.ForeignKey(User_info,related_name = "myid")
    user_b = models.ForeignKey(User_info,related_name = "friendid")
    typeid = models.IntegerField()
    memo_name = models.CharField(max_length = 20)
