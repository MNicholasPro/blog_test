#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:34
# @Author  : zhoumingkai
# @Site    : 
# @File    : department.py
# @Software: PyCharm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from booksdata.models.booktype import Booktype


# 新建作者
from login.forms import BooktypeModelForm


def add_booktype(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if request.method == "POST":
        booktype_form = BooktypeModelForm(request.POST)
        if booktype_form.is_valid():
            book_type = booktype_form.cleaned_data['book_type']
            if not booktype_form:
                message = "书籍类型不能为空！"
                return render(request, 'booktype/booktype.html', locals())
            else:
                new_author = Booktype()
                new_author.book_type = book_type
                new_author.save()
                message = "书籍类型添加成功！"
                return render(request, 'booktype/booktype.html', locals())
    booktype_form = BooktypeModelForm()
    return render(request, 'booktype/booktype.html', locals())


#查看书籍类型名称
def view_booktype(request):
    booktypeListSelect = Booktype.objects.all().values_list("id", "book_type")
    typeid = request.POST.get("b-typeid", "")
    if typeid:
        booktypeList = Booktype.objects.filter(id=typeid)
    else:
        booktypeList = Booktype.objects.all()
    return render(request, 'booktype/view_booktype.html', locals())


# 删除记录
def delete_booktype(requset, deleteId):
    Booktype.objects.filter(id=deleteId).delete()
    return HttpResponse(1)