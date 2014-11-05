from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'sp.publications.views.article', name='article'),
    url(r'^recipe/(\d+)/$', 'sp.publications.views.recipe', name='recipe'),
    url(r'^recipes/$', 'sp.publications.views.recipes', name='recipes'),
)
