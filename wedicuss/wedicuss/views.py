#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context,RequestContext
from django.shortcuts import render_to_response
from user_manage.manage import User_manage

import wedicuss.settings

# @csrf_protect
def welcome(request):
    if  request.user.is_authenticated():
        return HttpResponseRedirect("main/home/")
    um = User_manage()
    form = um.get_login_form()
    #form = login_form(initial={"login_name":"用户名","password":"密码"})
    return render_to_response("welcome.html", {'login_form': form},\
        context_instance=RequestContext(request))