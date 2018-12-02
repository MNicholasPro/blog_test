#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:54
# @Author  : zhoumingkai
# @Site    : 
# @File    : book_thoughts.py
# @Software: PyCharm


from __future__ import unicode_literals
from django.db import models
from django.db.models import CASCADE


class BookThoughtsReply(models.Model):
    class Meta(object):
        verbose_name = '书籍感悟'
        verbose_name_plural = '书籍感悟'

    book_thought_reply = models.CharField('书籍感悟回复', max_length=1024)
    book_thought_reply_author = models.CharField('书籍感悟回复作者', max_length=1024)
    deleted = models.IntegerField('删除', default=0)
    book_thought = models.ForeignKey("BookThoughts", on_delete=CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)