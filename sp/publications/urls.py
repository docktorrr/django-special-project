from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'sp.publications.views.article', name='article'),
)
