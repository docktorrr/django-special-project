from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'sp.contest.views.index', name='contest_index'),
    url(r'^$', 'sp.contest.views.index', name='contest_index'),
    url(r'^(\d+)/list/$', 'sp.contest.views.list', name='contest_list'),
    url(r'^list/$', 'sp.contest.views.list', name='contest_list'),
    url(r'^category/(\d+)/$', 'sp.contest.views.category', name='contest_category'),
    url(r'^(\d+)/start/$', 'sp.contest.views.contest_start', name='contest_start'),
    url(r'^start/$', 'sp.contest.views.contest_start', name='contest_start'),
    url(r'^(\d+)/add/$', 'sp.contest.views.contest_add', name='contest_add'),
    url(r'^(\d+)/add/ajax/$', 'sp.contest.views.contest_add_ajax', name='contest_add_ajax'),
    url(r'^add/$', 'sp.contest.views.contest_add', name='contest_add'),
    url(r'^add/ajax/$', 'sp.contest.views.contest_add_ajax', name='contest_add_ajax'),
    url(r'^work/(\d+)/$', 'sp.contest.views.contest_work', name='contest_work'),
    url(r'^done/$', TemplateView.as_view(template_name='%s/%s' % (settings.TEMPLATE_THEME, 'contest/contest_done.html')), name='contest_done'),
    url(r'^done/(\d+)/$', 'sp.contest.views.contest_done', name='contest_done'),
    url(r'^work/(\d+)/vote/$', 'sp.contest.views.vote', name='contest_vote'),
    url(r'^more_works/(\d+)/$', 'sp.contest.views.more_works', name='contest_more_works'),
    url(r'^more_works/$', 'sp.contest.views.more_works', name='contest_more_works'),
)