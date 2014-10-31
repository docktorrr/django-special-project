from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'sp.frontend.views.index', name='index'),   
    url(r'^login/$', 'sp.frontend.views.login', name='login'),
    url(r'^logout/$', 'sp.frontend.views.logout', name='logout'),
    url(r'^rating/$', 'sp.frontend.views.rating', name='rating'),   
)
