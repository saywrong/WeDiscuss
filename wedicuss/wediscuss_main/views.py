from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context,RequestContext
from django.shortcuts import render_to_response,render
from user_manage.manage import User_manage

# Create your views here.
# Create your views here.
def home(request):
    # if  not request.user.is_authenticated():
    #     return HttpResponseRedirect("/")
    user = request.user
    return render_to_response("main_frame.html",{"username":user.username},context_instance=RequestContext(request))