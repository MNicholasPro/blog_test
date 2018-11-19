#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 15:34
# @Author  : zhoumingkai
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from booksdata.views import zentao_department, zentao_personal, sonarqube_unittest, department, publisher, \
    author, booktype

urlpatterns = [
    # 数据管理
    url(r'^zentao-department/', zentao_department.load_department_page, name='load_department_page'),
    url(r'^zentao-personal/', zentao_personal.load_personal_page, name='load_personal_page'),
    url(r'^sonarqube-unittest/', sonarqube_unittest.load_unittest_page, name='load_unittest_page'),

    #部门管理
    url(r'^add-dept/', department.add_department, name='add_department'),
    url(r'^view-dept/', department.view_department, name='view_department'),
    #出版社管理
    url(r'^add-publisher/', publisher.add_publisher, name='add_publisher'),
    #作者管理
    url(r'^add-author/', author.add_author, name='add_author'),
    url(r'^view-author/', author.vies_author, name='vies_author'),
    #书籍类型管理
    url(r'^add-booktype/', booktype.add_booktype, name='add_booktype'),

]