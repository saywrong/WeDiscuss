from django.conf.urls import patterns, include, url

import wediscuss_main.views as wm_views

urlpatterns = patterns('',
    (r"^home/$",wm_views.home),
)