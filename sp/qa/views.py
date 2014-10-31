# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db import transaction
from django.utils import simplejson
from sp.qa.models import Question
from sp.qa.forms import QuestionForm

@transaction.commit_on_success
def question_add(request):
    if request.method=="POST" and request.is_ajax():
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=True)
            return HttpResponse(simplejson.dumps({'success':True, 'html': u'Ваш вопрос добавлен', 'question': question.id}), content_type="application/json")
        else:
            return HttpResponse(simplejson.dumps({'success':False, 'html': u'Не заполнены данные'}), content_type="application/json")
    else:
        return HttpResponse(simplejson.dumps({'success':False, 'html': u'Не валидный запрос'}), content_type="application/json")
