from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'sp.quiz.views.index', name='quiz_index'),
    url(r'^quiz/$', 'sp.quiz.views.quiz', name='quiz'),
    url(r'^quiz/(\d+)/$', 'sp.quiz.views.quiz', name='quiz'),
    url(r'^set_email/$', 'sp.quiz.views.set_email', name='quiz_set_email'),
    url(r'^quiz_send/$', 'sp.quiz.views.quiz_send', name='quiz_send'),
    url(r'^quiz_result/(\d+)/$', 'sp.quiz.views.quiz_result', name='quiz_result'),
    url(r'^quiz_finish/$', 'sp.quiz.views.quiz_finish', name='quiz_finish'),
    url(r'^get_scores/(\d+)/$', 'sp.quiz.views.get_scores', name='quiz_get_scores'),
)
