#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 15:34
# @Author  : zhoumingkai
# @Site    :
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from login import views

urlpatterns = [
    url(r'^index', views.index),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^logout', views.logout),
    url(r'^changepassword', views.changepassword),
]