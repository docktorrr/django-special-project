# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from sp.users.models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullname', 'social_profile_link', 'points', 'points_link')
    
    def fullname(self, obj):
        return obj.user.get_full_name()
    fullname.short_description = "Имя, Фамилия"

    def social_profile_link(self, obj):
        links = []
        for sa in obj.user.social_auth.all():
            if sa.provider == 'facebook':
                links.append('<a href="http://www.facebook.com/%s" target="_blank">http://www.facebook.com/%s</a>' % (sa.uid, sa.uid))
            if sa.provider == 'vk-oauth':
                links.append('<a href="http://www.vk.com/id%s" target="_blank">http://www.vk.com/id%s</a>' % (sa.uid, sa.uid))
            if sa.provider == 'twitter':
                links.append('<a href="https://twitter.com/account/redirect_by_id?id=%s" target="_blank">https://twitter.com/account/redirect_by_id?id=%s</a>' % (sa.uid, sa.uid))
            if sa.provider == 'odnoklassniki':
                links.append('<a href="http://www.odnoklassniki.ru/profile/%s" target="_blank">http://www.odnoklassniki.ru/profile/%s</a>' % (sa.uid, sa.uid))
            if sa.provider == 'google-oauth2':
                links.append(sa.uid)
        return "<br/>".join(links)
    social_profile_link.short_description = "Ссылка на профиль"
    social_profile_link.allow_tags = True

    def points_link(self, obj):
        return '<a href="%s?user=%s">Extra points</a>' % (reverse('admin:users_points_changelist'), obj.user.id)
    points_link.short_description = "Доп. баллы"
    points_link.allow_tags = True
    
admin.site.register(UserProfile, UserProfileAdmin)

class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'number', 'datetime', 'content_object')
admin.site.register(Points, PointsAdmin)
