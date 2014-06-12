from django.conf.urls import patterns, include, url

from django.contrib import admin

from wedicuss.views import * 

import wd_mainframe.views as mf_views
import wedicuss.settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wedicuss.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r"^$",welcome),
    
    url(r'^admin/', include(admin.site.urls)),

    url(r"^main/",include("wediscuss_main.urls")),
    url(r'^account/',include("user_manage.urls")),
)
