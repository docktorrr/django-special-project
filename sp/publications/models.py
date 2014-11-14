# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.encoding import force_unicode
from sp.utils import transliterate

# utils
def article_image_path(instance, filename):
    return "images/articles/%s" % transliterate(filename)


# model classes
class Rubric(models.Model):
    title = models.CharField(u'Название', max_length=250)

    class Meta:
        verbose_name = u"Рубрика"
        verbose_name_plural = u"Рубрики"

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(u'Название', max_length=250, db_index=True)
    description = models.TextField(u'Описание', null=True, blank=True)
    slug = models.SlugField(u'Транслитерация', max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = u"Тэг"
        verbose_name_plural = u"Тэги"

    def __unicode__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(u'Название', max_length=250)
    rubric = models.ForeignKey(Rubric, verbose_name=u'Рубрика', null=True, blank=True)
    annotation = models.TextField(u'Аннотация', null=True, blank=True)
    text = models.TextField(u'Текст')    
    is_published = models.BooleanField(u'Опубликовано', default=True, db_index=True)
    image = models.ImageField(u'Главное фото', upload_to=article_image_path, null=True, blank=True)
    preview = models.ImageField(u'Фото превью', upload_to=article_image_path, null=True, blank=True)
    pubdate = models.DateTimeField(u'Дата публикации', default=datetime.now, db_index=True)
    date_created = models.DateTimeField(u'Дата создания', auto_now_add=True, editable=False)
    date_changed = models.DateTimeField(u'Дата изменения', auto_now=True, editable=False)
    tags = models.ManyToManyField(Tag, verbose_name=u'Теги', blank=True)

    class Meta:
        verbose_name = u"Статья"
        verbose_name_plural = u"Статьи"

    def __unicode__(self):
        return self.title

class Recipe(Article):
    ingridients = models.TextField(u'Ингридиенты', null=True, blank=True)
    calories = models.IntegerField(u'Калории', db_index=True)
    cooking_time = models.IntegerField(u'Время приготовления (мин.)', db_index=True)
    portions = models.IntegerField(u'Количество порций', null=True, blank=True)

    class Meta:
        verbose_name = u"Рецепт"
        verbose_name_plural = u"Рецепты"

    def __unicode__(self):
        return self.title

    