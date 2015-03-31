from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'sp.frontend.views.index', name='index'),   
    url(r'^product/$', 'sp.frontend.views.product', name='product'),   
    url(r'^login/$', 'sp.frontend.views.login', name='login'),
    url(r'^logout/$', 'sp.frontend.views.logout', name='logout'),
    url(r'^register/$', 'sp.frontend.views.register', name='register'),
    url(r'^rating/$', 'sp.frontend.views.rating', name='rating'),
)
