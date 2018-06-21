# -*- coding: utf-8 -*-
'''
@author: April_Chou
@time: 2018/6/6 15:22
'''

from django.shortcuts import render, redirect

from login import forms


def load_unittest_page(request):
    if request.session.get('is_login', None) is None:
        login_form = forms.UserForm()
        return render(request, 'login/login.html', locals())
    return render(request, 'sonarqube/echarts_unittest.html')
