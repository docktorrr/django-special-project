# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from sp.publications.models import *


class RubricAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rubric, RubricAdmin)


class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)


class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label=u'Текст')
    
    class Meta:
        model = Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'pubdate', 'is_published')
    form = ArticleForm
    
admin.site.register(Article, ArticleAdmin)


class RecipeForm(ArticleForm):

    class Meta:
        model = Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'pubdate', 'is_published')
    form = RecipeForm
    
admin.site.register(Recipe, RecipeAdmin)




