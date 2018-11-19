#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:34
# @Author  : zhoumingkai
# @Site    : 
# @File    : department.py
# @Software: PyCharm


from django.shortcuts import render, redirect
from booksdata.models.department import Department


# 新建部门
from login.forms import DepartmentModelForm


def add_department(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if request.method == "POST":
        dept_form = DepartmentModelForm(request.POST)
        if dept_form.is_valid():
            dept_name = dept_form.cleaned_data['dept_name']
            if not dept_name:
                message = "部门名称不能为空！"
                return render(request, 'department/department.html', locals())
            else:
                new_dept = Department()
                new_dept.dept_name = dept_name
                new_dept.save()
                message = "部门名称添加成功！"
                return render(request, 'department/department.html', locals())
    dept_form = DepartmentModelForm()
    return render(request, 'department/department.html', locals())


#查看部门名称
def view_department(request):
    return render(request, 'department/view_department.html', locals())