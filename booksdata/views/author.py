#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:34
# @Author  : zhoumingkai
# @Site    : 
# @File    : department.py
# @Software: PyCharm


from django.shortcuts import render, redirect
from booksdata.models.department import Department


# 新建作者
from login.forms import AuthorModelForm

#新建作者名称
def add_author(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if request.method == "POST":
        author_form = AuthorModelForm(request.POST)
        if author_form.is_valid():
            author_name = author_form.cleaned_data['author_name']
            if not author_name:
                message = "作者名称不能为空！"
                return render(request, 'author/author.html', locals())
            else:
                new_author = Department()
                new_author.author_name = author_name
                new_author.save()
                message = "作者名称添加成功！"
                return render(request, 'author/author.html', locals())
    author_form = AuthorModelForm()
    return render(request, 'author/author.html', locals())

#查看作者名称
def vies_author(request):
    return render(request, 'author/view_author.html', locals())