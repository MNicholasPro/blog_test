# -*- coding: utf-8 -*-
'''
@author: April_Chou
@time: 2018/6/6 15:22
'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from login import forms


@login_required
def load_unittest_page(request):
    if request.session.get('is_login'):
        return render(request, 'sonarqube/echarts_unittest.html')
    else:
        login_form = forms.UserForm()
        return render(request, 'login/login.html', locals())