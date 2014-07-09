from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context,RequestContext
from django.shortcuts import render_to_response,render
from user_manage.manage import User_manage

from wediscuss_main.models import Discuss_group,Viewpoints
# Create your views here.
# Create your views here.
def home(request):
    # if  not request.user.is_authenticated():
    #     return HttpResponseRedirect("/")
    # user = request.user
    # assert(False)
    return render_to_response("home.html",{},context_instance=RequestContext(request))


def group(request,group_id):
    try:
        group_id=int(group_id)
    except ValueError:
        raise Http404()
    group_info = Discuss_group.get_sel_group_info(group_id)

    viewpoint_list = Viewpoints.get_rel_viewpoint_list(group_id)

    return render_to_response("group.html",
        {"group_info":group_info,"viewpoint_list":viewpoint_list},
        context_instance=RequestContext(request))

def create_group(request):
    # if  not request.user.is_authenticated():
    #     return HttpResponseRedirect("/")
    # user = request.user
    # assert(False)
    return render_to_response("create_group.html",{},context_instance=RequestContext(request))
