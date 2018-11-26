#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 20:12
# @Author  : zhoumingkai
# @Site    : 
# @File    : books.py
# @Software: PyCharm
import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import redirect, render

from booksdata.models.book import Book
from booksdata.models.booktype import Booktype
from booksdata.models.borrow_log import BorrowLog
from booksdata.models.department import Department
from booksdata.models.publisher import Publisher
from booksdata.models.author import Author
from django.views.decorators.csrf import csrf_exempt,csrf_protect


# 添加书籍
def add_book(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    booktypeList = Booktype.objects.filter().values_list("id", "book_type")
    publisherList = Publisher.objects.filter().values_list("id", "pub_name")
    authorList = Author.objects.filter().values_list("id", "author_name")
    return render(request, 'books/book.html', locals())


# 添加操作
def add_newbookdo(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    b_name = request.POST.get("b-name", " ")
    b_type = request.POST.get("b-type", " ")
    # b_pub = request.POST.get("b-pub", " ")
    # b_author = request.POST.get("b-author", " ")
    b_item = request.POST.get("b-item", " ")
    # booklist = Book.objects.create(book_name=b_name,book_type_id=b_type,book_publisher_id=b_pub,book_author_id=b_author,book_item=b_item)
    booklist = Book.objects.create(book_name=b_name,book_type_id=b_type,book_item=b_item)
    return render(request, 'books/book.html', locals())


#查看书籍
def view_newbooks(request):
    bookListSelect = Book.objects.filter(if_new=0).values_list("id", "book_name")
    departmentListSelect = Department.objects.all().values_list("id", "dept_name")
    bookId = request.POST.get("b-bookid", "")
    newbookList = []
    if  bookId != "":
        bookList = Book.objects.filter(if_new=0).filter(id=bookId).order_by("-id")
        newbookList = append_list(bookList)
    else:
        bookList = Book.objects.filter(if_new=0).order_by("-id")
        newbookList = append_list(bookList)
    return render(request, 'books/view_newbooks.html', locals())


#封装求作者、出版社、书籍类型方法
def append_list(bookList):
    newbookList = []
    for eachbooklist in bookList:
        booktypeList = Booktype.objects.filter(id=eachbooklist.book_type_id).values("book_type")[0].get("book_type")
        # publisherList = Publisher.objects.filter(id=eachbooklist.book_publisher_id).values("pub_name")[0].get("pub_name")
        # authorList = Author.objects.filter(id=eachbooklist.book_author_id).values("author_name")[0].get("author_name")
        eachbooklist.book_type_id = booktypeList
        # eachbooklist.book_publisher_id = publisherList
        # eachbooklist.book_author_id = authorList
        newbookList.append(eachbooklist)
    return newbookList



# 删除新书记录
def change_newbooks(request, deleteId):
    if Book.objects.filter(id=deleteId).update(if_new=1):
        return HttpResponse(1)
    else:
        return HttpResponse(0)


# 借用书籍
@csrf_exempt
def borrow_books(request):
    bookBorrower = request.session.get("user_name")
    dept_code = request.POST.get("dept_code", "")
    book_id = request.POST.get("book_id", "")
    borrow_item = request.POST.get("borrow_item", "")
    borrow_start = request.POST.get("borrow_start", "")
    borrow_end = request.POST.get("borrow_end", "")
    bookCount = Book.objects.filter(id=book_id)[0].book_count + 1

    if Book.objects.filter(id=book_id).update(book_count=bookCount,
                                             book_person=bookBorrower,
                                             book_state=2):
        bookName = Book.objects.filter(id=book_id)[0].book_name
        BorrowLog.objects.create(book_name=bookName,
                                 book_person=bookBorrower,
                                 borrow_start_time=borrow_start,
                                 borrow_end_time=borrow_end,
                                 book_item=borrow_item,
                                 book_person_dept_id=dept_code,
                                 book_id=book_id)
        return HttpResponse(1)
    else:
        return HttpResponse(0)

# 归还书籍
def return_books(request, bookId):
    bookBorrower = request.session.get("user_name")
    real_returnTime = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    book_person = Book.objects.filter(id=bookId).values("book_person")[0].get("book_person")
    if book_person == bookBorrower:
        if Book.objects.filter(id=bookId).update(book_state=0,book_person=''):
            BorrowLog.objects.filter(book_id=bookId).update(borrow_real_time=real_returnTime)
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    else:
        return HttpResponse(2)


#查看借阅日志
def view_book_log(request, bookId):
    borrowloglist = BorrowLog.objects.filter(book_id=bookId).order_by("-id")
    new_borrowloglist = []
    borrowloglist_size = len(borrowloglist)
    if(borrowloglist_size > 0):
        bookName = borrowloglist[0]
        for eachborrowlog in borrowloglist:
            department = Department.objects.filter(id=eachborrowlog.book_person_dept_id).values("dept_name")[0].get("dept_name")
            eachborrowlog.book_person_dept_name = department
            new_borrowloglist.append(eachborrowlog)
    return render(request, 'books/booklog.html', locals())


# 查看所有书籍
def view_allbooks(request):
    bookListSelect = Book.objects.all().values_list("id", "book_name")
    departmentListSelect = Department.objects.all().values_list("id", "dept_name")
    bookId = request.POST.get("b-bookid", "")
    newbookList_pre = []
    if  bookId:
        bookList = Book.objects.filter(id=bookId).order_by("-id")
        newbookList_pre = append_list(bookList)
    else:
        bookList = Book.objects.all().order_by("-id")
        newbookList_pre = append_list(bookList)
    newbookList = page_change(request, newbookList_pre)
    return render(request, 'books/view_allbooks.html', locals())


# 封装分页方法
def page_change(request, newbookList_pre):
    paginator = Paginator(newbookList_pre, 2)
    page = request.GET.get('page', 1)
    try:
        newbookList = paginator.page(page)
    except PageNotAnInteger:
        newbookList = paginator.page(1)
    except EmptyPage:
        newbookList = paginator.page(paginator.num_pages)
    return newbookList