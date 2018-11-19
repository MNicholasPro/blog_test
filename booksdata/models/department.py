#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/17 18:06
# @Author  : zhoumingkai
# @Site    : 
# @File    : department.py
# @Software: PyCharm


from __future__ import unicode_literals
from django.db import models


class Department(models.Model):
    class Meta(object):
        verbose_name = '部门'
        verbose_name_plural = '部门名称'

    dept_name = models.CharField('部门名称', max_length=128)
    deleted = models.IntegerField('删除', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)