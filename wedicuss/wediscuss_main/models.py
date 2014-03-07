from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 20)
    nickname = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.EmailField()
    state = models.IntegerField()

class Discuss_group(models.Model):
    name = models.CharField(max_length=30)
    creater = models.ForeignKey(User,related_name = "creater_id")
    create_time = models.DateTimeField()
    dead_line = models.DateTimeField()
    joiners = models.ManyToManyField(User,related_name = "joiners_id")
    dicuss_points = models.CharField(max_length = 100)
    state = models.IntegerField()
    desc = models.CharField(max_length = 140)
    is_public = models.BooleanField()
    password = models.CharField(max_length=8)
    is_anonymous = models.BooleanField()

class Users_viewpoint(models.Model):
    parrent = models.ForeignKey(Discuss_group)
    content = models.CharField(max_length = 140)
    dicuss_point = models.CharField(max_length = 20)
    pusher = models.ForeignKey(User)
    push_time = models.DateTimeField()
    up_nums = models.IntegerField()
    down_nums = models.IntegerField()

class Comments(models.Model):
    parrent = models.ForeignKey(Users_viewpoint)
    content = models.CharField(max_length = 140)
    pusher = models.ForeignKey(User)
    push_time = models.DateTimeField()
    action = models.IntegerField()

class User_relation(models.Model):
    my_id = models.ForeignKey(User,related_name = "myid")
    friend_id = models.ForeignKey(User,related_name = "friendid")
    typeid = models.IntegerField()
    memo_name = models.CharField(max_length = 20)

class message(models.Model):
    from_user = models.ForeignKey(User,related_name = "from_user_id")
    to_user = models.ForeignKey(User,related_name = "to_user_id")
    send_time = models.DateTimeField()
    typeid = models.IntegerField() 
    content = models.CharField(max_length = 140)