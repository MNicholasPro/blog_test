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

from booksdata.globalcontent import BOOK_STATE, BOOK_OK


class Book(models.Model):
    class Meta(object):
        verbose_name = '书籍'
        verbose_name_plural = '书籍管理'

    book_name = models.CharField('书籍名称', max_length=256)
    book_count = models.CharField('借阅次数', max_length=256, blank=True, null=True, default='')
    book_state = models.IntegerField('书籍状态', default=0, choices=BOOK_STATE)
    # book_type = models.IntegerField('书籍类型', default=0)
    book_type = models.ForeignKey('Booktype', on_delete=CASCADE)
    book_person = models.CharField('借用人', max_length=50, blank=True, null=True, default='')
    # book_person_dept = models.IntegerField('借用人部门', default=0)
    book_person_dept = models.ForeignKey('Department', on_delete=CASCADE)
    book_update_person = models.CharField('更新人', max_length=50, blank=True, null=True, default='')
    # book_publisher = models.IntegerField('出版商', default=0)
    book_publisher = models.ForeignKey('Publisher', on_delete=CASCADE)
    # book_author = models.CharField('书籍作者', max_length=16)
    book_author = models.ForeignKey('Author', on_delete=CASCADE)
    book_OK = models.IntegerField('书籍存在', default=0, choices=BOOK_OK)
    book_item = models.CharField('备注', max_length=512, blank=True, null=True, default='')
    deleted = models.IntegerField('删除', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)