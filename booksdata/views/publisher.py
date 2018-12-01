#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:34
# @Author  : zhoumingkai
# @Site    : 
# @File    : department.py
# @Software: PyCharm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from booksdata.models.publisher import Publisher


# 新建出版社
from login.forms import PublisherModelForm


def add_publisher(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if request.method == "POST":
        pub_form = PublisherModelForm(request.POST)
        if pub_form.is_valid():
            pub_name = pub_form.cleaned_data['pub_name']
            if not pub_name:
                message = "出版社名称不能为空！"
                return render(request, 'publisher/publisher.html', locals())
            else:
                new_pub = Publisher()
                new_pub.pub_name = pub_name
                new_pub.save()
                message = "出版社名称添加成功！"
                return render(request, 'publisher/publisher.html', locals())
    pub_form = PublisherModelForm()
    return render(request, 'publisher/publisher.html', locals())


#查看出版社名称
def view_publisher(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    publisherListSelect = Publisher.objects.all().values_list("id", "pub_name")
    pubid = request.POST.get("b-pubid", "")
    if pubid:
        publisherList = Publisher.objects.filter(id=pubid)
    else:
        publisherList = Publisher.objects.all()
    return render(request, 'publisher/view_publisher.html', locals())


# 删除记录
def delete_publisher(request, deleteId):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    Publisher.objects.filter(id=deleteId).delete()
    return HttpResponse(1)