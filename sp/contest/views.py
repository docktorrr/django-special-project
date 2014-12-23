# -*- coding: utf-8 -*-
import json
from datetime import date
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.contrib.auth import logout as logout_user
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from sp.contest import settings as opts
from sp.contest.models import Contest, Work, Vote, Tag
from sp.contest.forms import WorkForm
from sp.contest.decorators import active_contest_exists


def index(request, contest_id=None):
    contest = get_object_or_404(Contest, id=(contest_id or opts.ACTIVE_CONTEST))
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'contest/index.html'),
                              {
                              'contest': contest,
                              },
                              context_instance=RequestContext(request))


@active_contest_exists
@ensure_csrf_cookie
def list(request, contest_id=None):
    contest = get_object_or_404(Contest, id=(contest_id or opts.ACTIVE_CONTEST))
    works = Work.objects.filter(contest=contest, is_published=True)
    sort = None
    if 'sort' in request.GET and request.GET['sort'] == 'votes':
        sort = request.GET['sort']
        works = works.order_by('-count_votes')
    if 'sort' in request.GET and request.GET['sort'] == 'date_asc':
        sort = request.GET['sort']
        works = works.order_by('date_added')
    if 'sort' in request.GET and request.GET['sort'] == 'choice':
        sort = request.GET['sort']
        works = works.order_by('-editor_choice')

    paginator = Paginator(works, contest.page_size)
    page = 1
    if 'page' in request.GET:
        page = request.GET['page']
    try:
        works_page = paginator.page(page)
    except PageNotAnInteger:
        works_page = paginator.page(1)
    except EmptyPage:
        works_page = paginator.page(paginator.num_pages)

    user_work = None
    if request.user.is_authenticated():
        works = request.user.works.filter(contest=contest).all()
        if len(works) > 0 and works[0].date_added:
            user_work = works[0]
        
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'contest/list.html'),
                              {
                              'contest': contest,
                              'page': works_page,
                              'sort': sort,
                              'user_work': user_work,
                              },
                              context_instance=RequestContext(request))


@active_contest_exists
def contest_start(request, contest_id=None):
    contest = get_object_or_404(Contest, id=(contest_id or opts.ACTIVE_CONTEST))
    if request.user.is_authenticated():
        works = Work.objects.filter(contest=contest, user=request.user)
        if len(works) > 0:
            return HttpResponseRedirect(reverse('contest_work', args=(works[0].id,)))
            
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'contest/contest_start.html'),
                              {
                              'contest': contest
                              },
                              context_instance=RequestContext(request))                              

                              
@login_required
@active_contest_exists
@transaction.commit_on_success
def contest_add(request, contest_id=None):
    contest = get_object_or_404(Contest, id=(contest_id or opts.ACTIVE_CONTEST))
    if request.method == "POST":
        form = WorkForm(contest.name_input, contest.image_input, contest.text_input, contest.video_code_input, contest.video_link_input, contest.category_input, request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user
            work.contest = contest
            work.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('contest_done', args=(work.id,)))
    else:
        if contest.works_limit > 0:
            works = Work.objects.filter(contest=contest, user=request.user)
            if len(works) >= contest.works_limit:
                return HttpResponseRedirect(reverse('contest_work', args=(works[0].id,)))
        form = WorkForm(contest.name_input, contest.image_input, contest.text_input, contest.video_code_input, contest.video_link_input, contest.category_input)
            
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'contest/contest_add.html'),
                              {
                                'contest': contest,
                                'form': form
                               },
                              context_instance=RequestContext(request))                              

@login_required
@active_contest_exists
@transaction.commit_on_success
def contest_add_ajax(request, contest_id=None):
    contest = get_object_or_404(Contest, id=(contest_id or opts.ACTIVE_CONTEST))
    if request.method=="POST" and request.is_ajax():
        form = WorkForm(contest.name_input, contest.image_input, contest.text_input, contest.video_code_input, contest.video_link_input, contest.category_input, request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user
            work.contest = contest
            work.save()
            form.save_m2m()
            return HttpResponse(json.dumps({'success':True, 'html': u'Работа добавлена', 'work': work.id}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success':False, 'html': u'Не заполнены данные'}), content_type="application/json")
    else:
        if contest.works_limit > 0:
            works = Work.objects.filter(contest=contest, user=request.user)
            if len(works) >= contest.works_limit:
                return HttpResponse(json.dumps({'success':False, 'html': u'Вы уже добавили работу'}), content_type="application/json")
        return HttpResponse(json.dumps({'success':False, 'html': u'Не валидный запрос'}), content_type="application/json")

@active_contest_exists
@ensure_csrf_cookie
def contest_work(request, id):    
    work = get_object_or_404(Work, id=id)
    contest = work.contest
    try:
        prev = Work.objects.filter(contest=contest, is_published=True, date_added__gt=work.date_added).values_list('id', flat=True).order_by('date_added')[0]
    except IndexError:
        prev = None
    try:
        next = Work.objects.filter(contest=contest, is_published=True, date_added__lt=work.date_added).values_list('id', flat=True).order_by('-date_added')[0]
    except IndexError:
        next = None    
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'contest/contest_work.html'),
                              {'contest': contest,
                               'work': work,
                               'prev': prev,
                               'next': next,},
                              context_instance=RequestContext(request))

def contest_done(request, id):    
    work = get_object_or_404(Work, id=id)
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'contest/contest_done.html'),
                              {
                               'work': work
                              },
                              context_instance=RequestContext(request))

def vote(request, id):
    if request.is_ajax() and request.method=='POST':
        
        work = get_object_or_404(Work, id=id)
        
        if work.contest.stop_date and timezone.now() > work.contest.stop_date:
            return HttpResponse(json.dumps({'success':False, 'html': u'Голосование закончилось', 'id': work.id}), content_type="application/json")
                
        user = None
        if request.user.is_authenticated():
            user = request.user            
        ip = request.META["REMOTE_ADDR"]
        
        success = True
        error = ''
        if work.contest.unauth_voting:
            if Vote.objects.filter(work=work, ip_address=ip).count() > 0:
                success = False
                error = u'Вы уже голосовали'
        else:
            if not user:
                success = False
                error = u'Вы должны быть авторизованы'
            if work.user == user:
                success = False
                error = u'Вы не можете голосовать за свою работу'            
            if Vote.objects.filter(work=work, user=user).count() > 0:
                success = False
                error = u'Вы уже голосовали'

        if success:
            vote = Vote(work=work, ip_address=ip, user=user)
            vote.save()
            return HttpResponse(json.dumps({'success':True, 'html': u'Ваш голос учтен', 'id': work.id}), content_type="application/json")            
        else:
            return HttpResponse(json.dumps({'success':False, 'html': error, 'id': work.id}), content_type="application/json")
            
    else:
        return HttpResponseBadRequest()

def more_works(request, category_id=None):
    if request.is_ajax() and 'limit' in request.GET and 'offset' in request.GET:
        contest = get_object_or_404(Contest, id=opts.ACTIVE_CONTEST)
        limit = int(request.GET['limit'])
        offset = int(request.GET['offset'])
        works = Work.objects.filter(contest=contest, is_published=True)
        if category_id:
            works = works.filter(category=category_id)
        works = works[offset:offset+limit]        
        context = RequestContext(request)
        if len(works) > 0:
            rendered = render_to_string('%s/%s' % (settings.TEMPLATE_THEME, 'contest/photo_block.html'), {'contest': contest, 'works': works, 'STATIC_URL': context['STATIC_URL'], 'user': context['user']})
        else:
            rendered = ""
        last = False
        if len(works) < limit:
            last = True
        return HttpResponse(json.dumps({'success':True, 'html': rendered, 'last': last}), content_type="application/json") 
    else:
        return HttpResponseBadRequest()