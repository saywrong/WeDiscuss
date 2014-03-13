#coding:utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from user_manage.manage import User_manage

import wedicuss.settings


def welcome(request):
    t = get_template("login.html")
    um = User_manage()
    form = um.get_login_form()
    #form = login_form(initial={"login_name":"用户名","password":"密码"})
    return render_to_response("login.html", {'login_form': form})
    return HttpResponse(wedicuss.settings.STATIC_PATH)