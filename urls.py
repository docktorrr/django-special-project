from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('sp.frontend.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^contest/', include('sp.contest.urls')),
    url(r'^quiz/', include('sp.quiz.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^articles/', include('sp.publications.urls')),
    url(r'^qa/', include('sp.qa.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # only for development, on production use webserver rewrite
    url(r'^public/media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)