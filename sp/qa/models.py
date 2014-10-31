# -*- coding: utf-8 -*-
from django.db import models

class Question(models.Model):
    name = models.CharField(u'Имя', max_length=100)
    email = models.EmailField(u'E-mail')
    text = models.TextField(u'Вопрос')
    is_published = models.BooleanField(u'Опубликовано', default=False)
    answer = models.TextField(u'Ответ', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"Вопрос/Ответ"
        verbose_name_plural = u"Вопросы/Ответы"

    def __unicode__(self):
        return self.name
        