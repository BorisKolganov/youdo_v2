# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField('core.User', verbose_name=u'Профиль')
    about = models.TextField(verbose_name=u'О себе')
    skills = models.TextField(verbose_name=u'Умения')
    experience = models.TextField(verbose_name=u'Опыт')


class ServiceType(models.Model):
    name = models.CharField(max_length=250, verbose_name=u'Название')
    users = models.ManyToManyField('works.Employee', verbose_name=u'Специалисты', blank=True)

    class Meta:
        verbose_name = u'Вид работы'
        verbose_name_plural = u'Виды работ'

    def __unicode__(self):
        return self.name


class Service(models.Model):
    user = models.ForeignKey('core.User', verbose_name=u'Пользователь')
    employee = models.ForeignKey('works.Employee', verbose_name=u'Исполнитель', null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name=u'Название')
    description = models.TextField(verbose_name=u'Описание')
    price = models.IntegerField(verbose_name=u'Оплата')
    avatar = models.ImageField(verbose_name=u'Аватар', null=True, upload_to='avatars', default='avatars/default.jpg')
    type = models.ForeignKey('works.ServiceType', verbose_name=u'Тип услуги')


class Comment(models.Model):
    user = models.ForeignKey('core.User', verbose_name=u'Пользователь')
    service = models.ForeignKey('works.Service', verbose_name=u'услуга')
    text = models.TextField(verbose_name=u'Текст комментария')
    rating = models.SmallIntegerField(verbose_name=u'Оценка')
