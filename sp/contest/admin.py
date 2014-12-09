# -*- coding: utf-8 -*-
from django.contrib import admin
from sp.contest.models import *

def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = "Опубликовать выбранные работы"    

    
class ContestAdmin(admin.ModelAdmin):
    model = Contest
    list_display = ('title', 'is_active')
   
   
class WorkCategoryAdmin(admin.ModelAdmin):
    model = WorkCategory

    
class TagAdmin(admin.ModelAdmin):
    model = Tag

        
class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0
    readonly_fields = ('user', 'datetime', 'ip_address')


class WorkAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullname', 'social_profile_link', 'contest', 'date_added', 'is_published', 'count_votes')
    list_filter = ("contest",)
    inlines = [VoteInline,]
    actions = [make_published]

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

admin.site.register(Contest, ContestAdmin)
admin.site.register(WorkCategory, WorkCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Work, WorkAdmin)
