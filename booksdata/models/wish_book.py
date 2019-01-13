#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/17 15:27
# @Author  : zhoumingkai
# @Site    :
# @File    : book.py
# @Software: PyCharm


from __future__ import unicode_literals
from django.db import models


class WishBook(models.Model):
    class Meta(object):
        verbose_name = '心愿书籍'
        verbose_name_plural = '心愿书籍管理'

    book_name = models.CharField('书籍名称', max_length=256)
    book_author = models.CharField('书籍作者', max_length=32)
    book_item = models.CharField('备注', max_length=512, blank=True, null=True, default='')
    agree_count = models.IntegerField('点赞次数', default=0)
    deleted = models.IntegerField('删除', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)