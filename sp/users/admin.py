# -*- coding: utf-8 -*-
from django.contrib import admin
from sp.users.models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
admin.site.register(UserProfile, UserProfileAdmin)