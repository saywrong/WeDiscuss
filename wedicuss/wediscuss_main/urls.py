from django.conf.urls import patterns, include, url

import wediscuss_main.views as wm_views

urlpatterns = patterns('',
    (r"^home/$",wm_views.home),
    (r"^group/(\d)/$",wm_views.group),
    (r"^create_group/$",wm_views.create_group),
)