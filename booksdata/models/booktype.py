#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:08
# @Author  : zhoumingkai
# @Site    : 
# @File    : booktype.py
# @Software: PyCharm


from __future__ import unicode_literals
from django.db import models


class Booktype(models.Model):
    class Meta(object):
        verbose_name = '书籍类型'
        verbose_name_plural = '书籍类型'

    book_type = models.CharField('书籍类型', max_length=64)
    deleted = models.IntegerField('删除', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)