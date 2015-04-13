# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.db.models import Sum
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from sp.contest.models import Work
from sp.users.forms import AuthenticationForm, RegistrationForm


def index(request):
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'index.html'),
                              {},
                              context_instance=RequestContext(request))


def product(request):
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'product.html'),
                              {},
                              context_instance=RequestContext(request))


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login_user(request, form.get_user())
            if request.is_ajax():
                return HttpResponse(json.dumps({'success':True}), content_type="application/json")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER') or '/')
        else:
            if request.is_ajax():
                html = form.errors.as_text()
                return HttpResponse(json.dumps({'success': False, 'html':html}), content_type="application/json")
    else:
        form = AuthenticationForm()
    return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = user.get_profile()
            profile.avatar = form.cleaned_data["avatar"]
            profile.save()
            user = authenticate(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
            login_user(request, user)
            if request.is_ajax():
                return HttpResponse(json.dumps({'success': True}), content_type="application/json")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER') or '/')
        else:
            if request.is_ajax():
                html = form.errors.as_text()
                return HttpResponse(json.dumps({'success': False, 'html':html}), content_type="application/json")
    else:
        form = RegistrationForm()
    return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))


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
