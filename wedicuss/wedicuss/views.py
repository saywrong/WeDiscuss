#coding:utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from wedicuss.forms import login_form
import wedicuss.settings


def welcome(request):
    t = get_template("login.html")
    form = login_form(initial={"login_name":"用户名","password":"密码"})
    return render_to_response("login.html", {'form': form})
    return HttpResponse(wedicuss.settings.STATIC_PATH)