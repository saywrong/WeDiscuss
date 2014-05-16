from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Discuss_group(models.Model):
    name = models.CharField(max_length=30)
    creater = models.ForeignKey(User,related_name = "creater_id")
    create_time = models.DateTimeField()
    dead_line = models.DateTimeField()
    state = models.IntegerField()
    types = models.IntegerField()
    desc = models.CharField(max_length = 140)
    is_public = models.BooleanField()
    password = models.CharField(max_length=8)
    is_anonymous = models.BooleanField()
    addon_ids = models.CharField(max_length=30)

class Discuss_group_joiners(models.Model):
    discuss_group_id = models.ForeignKey(Discuss_group)
    user_id = models.ForeignKey(User)
    join_time = models.DateTimeField()

class Viewpoints(models.Model):
    parrent = models.ForeignKey(Discuss_group)
    content = models.CharField(max_length = 140)
    pusher = models.ForeignKey(User)
    push_time = models.DateTimeField()
    up_nums = models.IntegerField()
    down_nums = models.IntegerField()
    addon_ids = models.CharField(max_length=30)
