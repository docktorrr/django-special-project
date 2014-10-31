# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import logout as logout_user
from django.db.models import Sum
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from sp.contest.models import Work

def index(request):
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'index.html'),
                              {},
                              context_instance=RequestContext(request))

def login(request):
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'login.html'), 
                              {},
                              context_instance=RequestContext(request))

def logout(request):
    logout_user(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') or '/')                              
    
def rating(request):
    items = Work.objects.filter(is_published=True).values('user').annotate(rating=Sum('count_votes')).order_by('-rating')
    paginator = Paginator(items, 20)
    page = 1
    if 'page' in request.GET:
        page = request.GET['page']
    try:
        rating_page = paginator.page(page)
    except PageNotAnInteger:
        rating_page = paginator.page(1)
    except EmptyPage:
        rating_page = paginator.page(paginator.num_pages)
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'rating.html'),
                              {'page': rating_page},
                              context_instance=RequestContext(request))
    