#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 15:51
# @Author  : zhoumingkai
# @Site    : 
# @File    : publisher.py
# @Software: PyCharm


from __future__ import unicode_literals
from django.db import models


class Publisher(models.Model):
    class Meta(object):
        verbose_name = '出版商'
        verbose_name_plural = '出版商'

    pub_name = models.CharField('出版商', max_length=128)
    deleted = models.IntegerField('删除', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)