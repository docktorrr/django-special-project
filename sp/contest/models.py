# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode
from sp.utils import transliterate

# utils
def contest_image_path(instance, filename):
    return "images/contest/%s" % transliterate(filename)


# model classes
class Contest(models.Model):
    
    title = models.CharField(u'Название', max_length=250)
    description = models.TextField(u'Описание')
    is_active = models.BooleanField(u'Активный', default=False)
    page_size = models.IntegerField(u'Размер страницы', default=10)
    unauth_voting = models.BooleanField(u'Возможность неавторизованного голосования', default=False)
    name_input = models.BooleanField(u'Ввод названия', default=True)
    image_input = models.BooleanField(u'Ввод изображения', default=True)
    text_input = models.BooleanField(u'Ввод текста', default=True)
    video_code_input = models.BooleanField(u'Ввод кода видео', default=False)
    video_link_input = models.BooleanField(u'Ввод ссылки видео', default=False)
    category_input = models.BooleanField(u'Ввод категории', default=False)
    works_limit = models.IntegerField(u'Лимит работ для пользователя', default=1, help_text=u'0 - без ограничений')
    moderator_emails = models.TextField(u'E-mail адреса модераторов', blank=True, null=True)
    stop_date = models.DateTimeField(u'Дата окончания', blank=True, null=True)

    class Meta:
        verbose_name = u"Конкурс"
        verbose_name_plural = u"Конкурсы"

    def __unicode__(self):
        return self.title

        
class WorkCategory(models.Model):
    name = models.CharField(u'Название', max_length=250)
    description = models.TextField(u'Описание', blank=True, null=True)
    property1 = models.CharField(u'Дополнительное свойство 1', max_length=500)
    property2 = models.CharField(u'Дополнительное свойство 2', max_length=500)
    property3 = models.CharField(u'Дополнительное свойство 3', max_length=500)

    class Meta:
        verbose_name = u"Категория конкурсной работы"
        verbose_name_plural = u"Категории конкурсной работы"

    def __unicode__(self):
        return self.name

        
class Work(models.Model):
    contest = models.ForeignKey(Contest, related_name='works', verbose_name=u'Конкурс')
    user = models.ForeignKey(User, related_name='works', verbose_name=u'Пользователь')
    name = models.CharField(u'Название', max_length=256, blank=True, null=True)
    category = models.ForeignKey(WorkCategory, related_name='works', verbose_name=u'Категория', null=True, blank=True)
    count_votes = models.IntegerField(u'Количество голосов', default=0)
    is_published = models.BooleanField(u'Опубликовано', default=False, db_index=True)
    date_added = models.DateTimeField(u'Дата добавления', auto_now_add=True)
    image = models.ImageField(u'Фотография', upload_to=contest_image_path, blank=True, null=True)
    text = models.TextField(u'Описание', blank=True, null=True)
    video_code = models.TextField(u'Код видео', blank=True, null=True)
    video_link = models.CharField(u'Ссылка на видео', max_length=256, blank=True, null=True)
    editor_choice = models.BooleanField(u'Выбор редакции', default=False, db_index=True)
    
    class Meta:
        ordering = ['-date_added']
        verbose_name = u"Конкурсная работа"
        verbose_name_plural = u"Конкурсные работы"

    def __unicode__(self):
        return u'%s' % self.user.username

    def place(self):
        return Work.objects.filter(contest__id=self.contest.id, date_added__isnull=False, is_published=True).filter(models.Q(count_votes__gt = self.count_votes) | models.Q(count_votes = self.count_votes, date_added__lt = self.date_added)).count() + 1
        
    def extra_field_values(self):
        data = {}
        for item in self.extra_values.all():
            data[item.field.name] = item.value
        return data
        
    
class Vote(models.Model):
    work = models.ForeignKey(Work, related_name='votes')
    datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.IPAddressField()
    user = models.ForeignKey(User, related_name='votes', verbose_name=u'Пользователь', null=True)

    class Meta:
        verbose_name = u'Голос'
        verbose_name_plural = u'Голоса'
    
    def save(self):
        if not self.id:
            self.work.count_votes += 1
            self.work.save()
        super(Vote, self).save()

    @classmethod
    def vote_delete(cls, instance, sender, **kwargs):
        instance.work.count_votes = instance.work.count_votes - 1
        instance.work.save()

models.signals.pre_delete.connect(Vote.vote_delete, sender=Vote)        
