# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    title = models.CharField(u'Название', max_length=150)
    image = models.ImageField(u'Изображение', upload_to='quiz_images', null=True, blank=True)
    is_test = models.BooleanField(u'Это тест', default=True)

    class Meta:
        verbose_name = u"Викторина / тест"
        verbose_name_plural = u"Викторины / тесты"

    def __unicode__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', verbose_name=u'Викторина/тест')
    text = models.CharField(u'Вопрос', max_length=250)
    image = models.ImageField(u'Изображение', upload_to='quiz_images', null=True, blank=True)

    class Meta:
        verbose_name = u"Вопрос"
        verbose_name_plural = u"Вопросы"

    def __unicode__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', verbose_name=u'Вариант ответа')
    text = models.CharField(u'Текст', max_length=250)
    image = models.ImageField(u'Изображение', upload_to='quiz_images', null=True, blank=True)
    score = models.IntegerField(u'Баллы', default=0)

    class Meta:
        verbose_name = u"Вариант ответа"
        verbose_name_plural = u"Варианты ответа"

    def __unicode__(self):
        return self.text


class ScoreVariant(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='score_variants', verbose_name=u'Викторина/тест')
    from_score = models.IntegerField(u'Минимальный балл')
    upto_score = models.IntegerField(u'Максимальный балл')
    title = models.CharField(u'Название результата', max_length=150)
    text = models.TextField(u'Текст результата')
    image = models.ImageField(u'Изображение', upload_to='quiz_images', null=True, blank=True)
    
    class Meta:
        verbose_name = u"Вариант результаты"
        verbose_name_plural = u"Варианты результата"

    def __unicode__(self):
        return '%s (%s-%s)' % (self.title, self.from_score, self.upto_score)


class UserScore(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='scores', verbose_name=u'Викторина/тест')
    answers = models.ManyToManyField(Answer, verbose_name=u'Ответы')
    score = models.IntegerField(u'Сумма баллов')
    finished = models.BooleanField(u'Закончил', default=False)
    email = models.EmailField(u'E-mail пользователя', null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    date_added = models.DateTimeField(u'Дата', auto_now_add=True)

    class Meta:
        verbose_name = u"Результат пользователя"
        verbose_name_plural = u"Результаты пользователей"

    def __unicode__(self):
        if self.user:
            return self.user.username
        return self.email
