#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/17 15:27
# @Author  : zhoumingkai
# @Site    :
# @File    : book.py
# @Software: PyCharm


from __future__ import unicode_literals
from django.db import models
from django.db.models import CASCADE


class AgreeRecord(models.Model):
    class Meta(object):
        verbose_name = '点赞记录'
        verbose_name_plural = '心愿书籍点赞记录'

    wish_id = models.ForeignKey('WishBook', on_delete=CASCADE)
    agree_person = models.CharField('点赞人', max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)