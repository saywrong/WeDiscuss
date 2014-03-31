from django.conf.urls import patterns, include, url

from django.contrib import admin

from wedicuss.views import * 
import user_manage.views as um_views
import wedicuss.settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wedicuss.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r"^$",welcome),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': wedicuss.settings.STATIC_PATH}), 
    (r"^login_auth/",um_views.login_auth),
    (r"^login/$",um_views.login),
    (r"^register/$",um_views.register),
)
