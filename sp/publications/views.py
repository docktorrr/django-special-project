# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sp.publications.models import *


def article(request, id):
    article = get_object_or_404(Article, id=id)
    return render_to_response('publications/article.html', {'article': article}, context_instance=RequestContext(request))