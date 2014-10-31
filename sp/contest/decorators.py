# -*- coding: utf-8 -*-
from django.http import HttpResponse
from sp.contest import settings as opts


def active_contest_exists(func):
    def inner(request, *args, **kwargs):
        if not hasattr(opts, 'ACTIVE_CONTEST') and not kwargs['contest_id']:
            return HttpResponse('Improperly configured: Pass contest ID arg or set active contest ID in settings')
        return func(request, *args, **kwargs)
    return inner