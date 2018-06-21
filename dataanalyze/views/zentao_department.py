# -*- coding: utf-8 -*-
'''
@author: April_Chou
@time: 2018/6/6 15:22
'''

from django.shortcuts import render

from login import forms


def load_department_page(request):
    if request.session.get('is_login') is None:
        login_form = forms.UserForm()
        return render(request, 'login/login.html', locals())
    return render(request, 'zentao/echarts_department.html')