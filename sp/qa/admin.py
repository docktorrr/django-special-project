# -*- coding: utf-8 -*-
from django.contrib import admin
from sp.qa.models import Question

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('name', 'is_published', 'date_added')
    ordering = ('-date_added',)
admin.site.register(Question, QuestionAdmin)
    