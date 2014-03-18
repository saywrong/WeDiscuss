#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from user_manage.manage import User_manage

import wedicuss.settings
from django.contrib import auth
# Create your views here.

def login_auth(request):
    username = request.POST.get("username",None)
    password = request.POST.get("password",None)

    user = auth.authenticate(username = username,password = password)
    if user != None:
        auth.login(request,user)
        return HttpResponse("correct")
    else:
        return HttpResponseRedirect("/")