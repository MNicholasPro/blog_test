#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 15:34
# @Author  : zhoumingkai
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from booksdata.views import department, publisher, author, booktype, books

urlpatterns = [

    #部门管理
    url(r'^add-dept/', department.add_department, name='add_department'),
    url(r'^view-dept/', department.view_department, name='view_department'),
    url(r'^delete-dept/(\d+)', department.delete_dept, name='delete_dept'),
    #出版社管理
    url(r'^add-publisher/', publisher.add_publisher, name='add_publisher'),
    url(r'^view-publisher/', publisher.view_publisher, name='view_publisher'),
    url(r'^delete-publisher/(\d+)', publisher.delete_publisher, name='delete_publisher'),
    #作者管理
    url(r'^add-author/', author.add_author, name='add_author'),
    url(r'^view-author/', author.vies_author, name='vies_author'),
    url(r'^delete-author/(\d+)', author.delete_author, name='delete_author'),
    #书籍类型管理
    url(r'^add-booktype/', booktype.add_booktype, name='add_booktype'),
    url(r'^view-booktype/', booktype.view_booktype, name='view_booktype'),
    url(r'^delete-booktype/(\d+)', booktype.delete_booktype, name='delete_booktype'),

    # 新书籍推荐
    url(r'^add-newbook/', books.add_book, name='add_book'),
    url(r'^add-newbookdo/', books.add_newbookdo, name='add_newbookdo'),
    url(r'^view-newbooks/', books.view_newbooks, name='view_newbooks'),
    url(r'^view-allbooks/', books.view_allbooks, name='view_allbooks'),
    url(r'^view-books/', books.view_newbooks, name='view_newbooks'),
    url(r'^change-books/(\d+)', books.change_newbooks, name='change_newbooks'),
    url(r'^borrow-books/', books.borrow_books, name='borrow_books'),
    url(r'^return-books/(\d+)', books.return_books, name='return_books'),
    url(r'^view-book_log/(\d+)', books.view_book_log, name='view_book_log'),

]