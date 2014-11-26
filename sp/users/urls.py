from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^profile/$', 'sp.users.views.profile', name='user_profile'),
    url(r'^set_extra_points/(\d+)/(\w+)/(\d+)/$', 'sp.users.views.set_extra_points', name='user_set_extra_points'),
)