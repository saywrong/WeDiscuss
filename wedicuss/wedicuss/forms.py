#coding:utf-8
from django import forms

class login_form(forms.Form):
    login_name = forms.CharField(label="用户名")
    password = forms.CharField(label="密码",widget = forms.PasswordInput)