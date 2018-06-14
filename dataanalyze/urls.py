#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 15:34
# @Author  : zhoumingkai
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from dataanalyze.views import zentao_department, zentao_personal, sonarqube_unittest

urlpatterns = [
    # 数据管理
    url(r'^zentao-department/', zentao_department.load_department_page, name='load_department_page'),
    url(r'^zentao-personal/', zentao_personal.load_personal_page, name='load_personal_page'),
    url(r'^sonarqube-unittest/', sonarqube_unittest.load_unittest_page, name='load_unittest_page'),
]