# -*- coding: utf-8 -*-
import urllib2
from django.core.files.base import ContentFile
from social_auth.backends.twitter import TwitterBackend
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.contrib.vk import VKOAuth2Backend
from social_auth.backends.contrib.odnoklassniki import OdnoklassnikiBackend
from social_auth.backends.google import GoogleOAuth2Backend


def get_user_avatar(request, backend, response, social_user, uid, user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
    elif backend.__class__ == TwitterBackend:
        url = response.get('profile_image_url', '').replace('_normal', '')
    elif backend.__class__ == VKOAuth2Backend:
        url = response.get('user_photo')      
    elif backend.__class__ == OdnoklassnikiBackend:
        url = response.get('pic_2')
        if 'stub' in url:
            image_url = None
    if url:
        profile = user.get_profile()
        avatar_content = urllib2.urlopen(url)
        image_name = profile.avatar.field.upload_to + '/' + str(user.id) + '.' + avatar_content.headers.subtype
        profile.avatar.save(image_name, ContentFile(avatar_content.read()))
        profile.save()