#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 12:33
# @Author  : zhoumingkai
# @Site    : 
# @File    : borrow_log.py
# @Software: PyCharm


from __future__ import unicode_literals
from django.db import models
from django.db.models import CASCADE


class BorrowLog(models.Model):
    class Meta(object):
        verbose_name = '书籍日志'
        verbose_name_plural = '书籍借用日志'

    book_name = models.CharField('书籍名称', max_length=256)
    book_person = models.CharField('借用人', max_length=50)
    # book_person_dept = models.IntegerField('借用人部门', default=0)
    book_person_dept = models.ForeignKey('Department', on_delete=CASCADE)
    book_person_dept_name = models.CharField('部门名称', max_length=16, blank=True, null=True, default='')
    borrow_start_time = models.CharField('开始借阅时间', max_length=50)
    borrow_end_time = models.CharField('预计归还时间', max_length=50)
    borrow_real_time = models.CharField('实际归还时间', max_length=50)
    book_item = models.CharField('备注', max_length=512, blank=True, null=True, default='')
    book = models.ForeignKey('Book', on_delete=CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)