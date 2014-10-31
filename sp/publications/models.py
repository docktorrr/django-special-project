# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.encoding import force_unicode


# utils
def transliterate(text):
    TRANS_MAP = { u'а':'a', u'б':'b', u'в':'v', u'г':'g', u'д':'d', u'е':'e', u'ё':'e', u'ж':'zh',
              u'з':'z', u'и':'i', u'й':'i', u'к':'k', u'л':'l', u'м':'m', u'н':'n', u'о':'o',
              u'п':'p', u'р':'r', u'с':'s', u'т':'t', u'у':'u', u'ф':'f', u'х':'h', u'ц':'ts',
              u'ч':'ch', u'ш':'sh', u'щ':'sch', u'ъ':'j', u'ы':'y', u'ь':'j', u'э':'e', u'ю':'yu',
              u'я':'ya', u' ':'-', u'_':'_', u'№': '', u'"': '', u'\'': '', u'«': '', u'»': ''}

    if not isinstance(text, unicode):
        text = force_unicode(text)
    text = text.lower()
    retval = []
    for t in text:
        translation = TRANS_MAP.get(t,None)
        if translation is not None:
            retval += translation
        else:
            retval += t
    retval = "".join(retval)
    return retval


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
    tags = models.ManyToManyField(Tag, verbose_name=u'Теги')

    class Meta:
        verbose_name = u"Статья"
        verbose_name_plural = u"Статьи"

    def __unicode__(self):
        return self.title

class Recipe(Article):
    ingridients = models.TextField(u'Ингридиенты', null=True, blank=True)
    calories = models.IntegerField(u'Калории', db_index=True)
    cooking_time = models.IntegerField(u'Время приготовления (мин.)', db_index=True)

    class Meta:
        verbose_name = u"Рецепт"
        verbose_name_plural = u"Рецепты"

    def __unicode__(self):
        return self.title

    