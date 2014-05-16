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
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length = 20)
    state = models.IntegerField()
    coins = models.IntegerField()
    group =  models.ForeignKey(User_group)

    def __unicode__(self):
        return u"name:%s state:%d" \
        %(self.user.username,self.state)


class User_relation(models.Model):
    user_a = models.ForeignKey(User,related_name = "myid")
    user_b = models.ForeignKey(User,related_name = "friendid")
    typeid = models.IntegerField()
    memo_name = models.CharField(max_length = 20)
