from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^add/$', 'sp.qa.views.question_add', name='qa_add'),
)