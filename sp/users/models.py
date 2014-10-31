# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    avatar = models.ImageField(u'Аватар', upload_to='images/avatars/')

    class Meta:
        verbose_name = u"Профиль пользователя"
        verbose_name_plural = u"Профили пользователя"

    def __unicode__(self):
        return self.user.username
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
models.signals.post_save.connect(create_user_profile, sender=User)