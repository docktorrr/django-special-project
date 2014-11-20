# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum

# utils
def recount_points(profile):
    contest_points = profile.user.works.filter(is_published=True).aggregate(votes=Sum('count_votes'))['votes'] or 0
    extra_points = profile.user.user_points.all().aggregate(sum=Sum('number'))['sum'] or 0
    profile.points = contest_points + extra_points
    profile.save()


# models
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    avatar = models.ImageField(u'Аватар', upload_to='images/avatars/', blank=True, null=True)
    points = models.IntegerField(u'Баллы', default=0)

    class Meta:
        ordering = ['-points']
        verbose_name = u"Профиль пользователя"
        verbose_name_plural = u"Профили пользователя"

    def __unicode__(self):
        return self.user.username
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
models.signals.post_save.connect(create_user_profile, sender=User)

class Points(models.Model):
    user = models.ForeignKey(User, related_name='user_points', verbose_name=u'Пользователь')
    number = models.IntegerField(u'Количество')
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.CharField(u'За что', max_length=256, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        verbose_name = u"Баллы"
        verbose_name_plural = u"Баллы"

    def save(self):
        if not self.id:
            profile = self.user.get_profile()
            profile.points = profile.points + self.number
            profile.save()
        super(Points, self).save()

    @classmethod
    def points_delete(cls, instance, sender, **kwargs):
        profile = instance.user.get_profile()
        profile.points = profile.points - instance.number
        profile.save()

models.signals.pre_delete.connect(Points.points_delete, sender=Points)        
        