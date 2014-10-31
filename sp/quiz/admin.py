# -*- coding: utf-8 -*-
from django.contrib import admin
from sp.quiz.models import *


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


class ScoreVariantInline(admin.TabularInline):
    model = ScoreVariant


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ScoreVariantInline]
admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
admin.site.register(Question, QuestionAdmin)


class UserScoreAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'email', 'score', 'date_added')
admin.site.register(UserScore, UserScoreAdmin)
    



