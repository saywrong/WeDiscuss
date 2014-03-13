#coding:utf-8
from django.template.loader import get_template
from django.template import Context

from user_manage.models import User_group,User_info,User_relation
from user_manage.forms import login_form,create_user_form

class User_manage:

    def get_login_form(self):
        t = get_template("login_form.html")
        c = Context({"form":login_form})
        return t.render(c)

    def get_createuser_form(self):
        t = get_template("create_user.html")
        c = Context({"form":create_user_form})
        return t.render(c)
        pass

    def get_modifyuser_form(self):
        pass

    def get_user_info(self,username):
        pass

    def create_user(self,User_info):
        pass

    def create_user_info(self,):
        pass

    def verify_password(self,username,password):
        pass

