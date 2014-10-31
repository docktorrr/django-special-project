# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
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


def contest_image_path(instance, filename):
    return "images/contest/%s" % transliterate(filename)


# model classes
class Contest(models.Model):
    title = models.CharField(u'Название', max_length=250)
    description = models.TextField(u'Описание')
    is_active = models.BooleanField(u'Активный', default=False)
    page_size = models.IntegerField(u'Размер страницы', default=10)
    name_input = models.BooleanField(u'Ввод названия', default=True)
    image_input = models.BooleanField(u'Ввод изображения', default=True)
    text_input = models.BooleanField(u'Ввод текста', default=True)
    video_code_input = models.BooleanField(u'Ввод кода видео', default=False)
    video_link_input = models.BooleanField(u'Ввод ссылки видео', default=False)
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
    category = models.ForeignKey(u'Категория', null=True)
    count_votes = models.IntegerField(u'Количество голосов', default=0)
    is_published = models.BooleanField(u'Опубликовано', default=False, db_index=True)
    date_added = models.DateTimeField(u'Дата добавления', auto_now_add=True)
    image = models.ImageField(u'Фотография', upload_to=contest_image_path, blank=True, null=True)
    text = models.TextField(u'Описание', blank=True, null=True)
    video_code = models.TextField(u'Код видео', blank=True, null=True)
    video_link = models.CharField(u'Ссылка на видео', max_length=256, blank=True, null=True)

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
