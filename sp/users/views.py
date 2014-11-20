# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from sp.users.models import Points

@login_required
def set_extra_points(request, number, model_name, object_id):
    if request.is_ajax():
        user = request.user
        content_type = ContentType.objects.get(model=model_name)
        if Points.objects.filter(user=user, content_type=content_type, object_id=object_id).count() == 0:
            new = Points(user=user, content_type=content_type, object_id=object_id, number=int(number))
            new.save()
        return HttpResponse(json.dumps({'success':True, 'points': user.get_profile().points}), content_type="application/json")
    else:
        return HttpResponseBadRequest()
        

