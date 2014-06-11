#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context,RequestContext
from django.shortcuts import render_to_response
from user_manage.manage import User_manage

import wedicuss.settings
from django.contrib import auth
# Create your views here.

def login_auth(request):
    # if  request.user.is_authenticated():
    #     return HttpResponseRedirect("/first_page/")
        
    if not request.POST:
        error = False
        um = User_manage()
        form = um.get_login_form()
        return render_to_response("login.html", {'login_form': form,'error':error},\
            context_instance=RequestContext(request))

    username = request.POST.get("username",None)
    password = request.POST.get("password",None)

    user = auth.authenticate(username = username,password = password)
    if user != None:
        auth.login(request,user)
        return HttpResponseRedirect("/first_page/")
    else:
        error = True
        um = User_manage()
        form = um.get_login_form()  
        return render_to_response("login.html", {'login_form': form,'error':error},\
            context_instance=RequestContext(request))

# def login(request):
#     error = False
#     um = User_manage()
#     form = um.get_login_form()
#     #form = login_form(initial={"login_name":"用户名","password":"密码"})
#     return render_to_response("login.html", {'login_form': form,'error':error},\
#         context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    #assert False
    return HttpResponseRedirect("/")

def register(request):
    return HttpResponse("register page")