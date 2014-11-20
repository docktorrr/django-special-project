from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^set_extra_points/(\d+)/(\w+)/(\d+)/$', 'sp.users.views.set_extra_points', name='user_set_extra_points'),
)