#coding:utf-8
from django import forms

class login_form(forms.Form):
    login_name = forms.CharField(label="用户名")
    password = forms.CharField(label="密码",widget = forms.PasswordInput)

class create_user_form(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码",widget = forms.PasswordInput)
    first_name = forms.CharField(label="名字")
    last_name = forms.CharField(label="姓氏")
    email = forms.EmailField(label="邮件")
    nickname = forms.EmailField(label="昵称")