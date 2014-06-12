from django.conf.urls import patterns, include, url

import user_manage.views as um_views

urlpatterns = patterns('',
    (r"^login/$",um_views.login_auth),
    (r"^signup/$",um_views.register),
    (r"^logout/$",um_views.logout),
)
