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

from booksdata.models.agree_record import AgreeRecord
from booksdata.models.book import Book
from booksdata.models.book_thoughts import BookThoughts
from booksdata.models.book_thoughts_reply import BookThoughtsReply
from booksdata.models.booktype import Booktype
from booksdata.models.borrow_log import BorrowLog
from booksdata.models.department import Department
from booksdata.models.publisher import Publisher
from booksdata.models.author import Author
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from booksdata.models.wish_book import WishBook
from login.forms import WishBookModelForm


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
    booktypeList = Booktype.objects.filter().values_list("id", "book_type")
    return render(request, 'books/book.html', locals())


#查看书籍
def view_newbooks(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    bookListSelect = Book.objects.filter(if_new=0).values_list("id", "book_name")
    departmentListSelect = Department.objects.all().values_list("id", "dept_name")
    bookId = request.POST.get("b-bookid", "")
    newbookList = []
    if  bookId != "":
        bookList = Book.objects.filter(if_new=0).filter(id=bookId).order_by("-id")
        newbookList = append_list(request, bookList)
    else:
        bookList = Book.objects.filter(if_new=0).order_by("-id")
        newbookList = append_list(request, bookList)
    return render(request, 'books/view_newbooks.html', locals())


#封装求作者、出版社、书籍类型方法
def append_list(request, bookList):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
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
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if Book.objects.filter(id=deleteId).update(if_new=1):
        return HttpResponse(1)
    else:
        return HttpResponse(0)


# 借用书籍
@csrf_exempt
def borrow_books(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
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
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
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
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
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
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    bookListSelect = Book.objects.all().values_list("id", "book_name")
    departmentListSelect = Department.objects.all().values_list("id", "dept_name")
    bookId = request.POST.get("b-bookid", "")
    newbookList_pre = []
    if  bookId:
        bookList = Book.objects.filter(id=bookId).order_by("-id")
        newbookList_pre = append_list(request, bookList)
    else:
        bookList = Book.objects.all().order_by("-id")
        newbookList_pre = append_list(request, bookList)
    newbookList = page_change(request, newbookList_pre)
    return render(request, 'books/view_allbooks.html', locals())


# 封装分页方法
def page_change(request, newbookList_pre):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    paginator = Paginator(newbookList_pre, 10)
    page = request.GET.get('page', 1)
    try:
        newbookList = paginator.page(page)
    except PageNotAnInteger:
        newbookList = paginator.page(1)
    except EmptyPage:
        newbookList = paginator.page(paginator.num_pages)
    return newbookList


# 心愿书
def add_whish_books(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if request.method == "POST":
        wishbook_form = WishBookModelForm(request.POST)
        if wishbook_form.is_valid():
            book_name = wishbook_form.cleaned_data['book_name']
            book_author = wishbook_form.cleaned_data['book_author']
            book_item = wishbook_form.cleaned_data['book_item']
            if not wishbook_form:
                message = "书籍相关内容不能为空！"
                return render(request, 'books/wish_book.html', locals())
            else:
                new_wish_book = WishBook()
                new_wish_book.book_name = book_name
                new_wish_book.book_author = book_author
                new_wish_book.book_item = book_item
                new_wish_book.save()
                message = "书籍类型添加成功！"
                return render(request, 'books/wish_book.html', locals())
    wishbook_form = WishBookModelForm()
    return render(request, 'books/wish_book.html', locals())


# 查看所有心愿书籍
def view_whish_books(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    wishbookList = WishBook.objects.filter(deleted=0)
    return render(request, 'books/view_wishbooks.html', locals())


# 删除心愿书记录
def delete_wish_book(request, deleteId):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if WishBook.objects.filter(id=deleteId).update(deleted=1):
        return HttpResponse(1)
    else:
        return HttpResponse(0)


# 新增读书感悟
def add_book_thoughts_page(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    bookListSelect = Book.objects.all().values_list("id", "book_name")
    return render(request, 'books/book_thoughts.html', locals())


# 操作新增
def add_book_thoughts(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    book_id = request.POST.get("b-bookid", "")
    book_title = request.POST.get("b-Title", "")
    book_thought = request.POST.get("b-thought", "")
    book_thought_author = request.session.get("user_name")
    book_name = Book.objects.filter(id=book_id).values("book_name")[0].get("book_name")
    BookThoughts.objects.create(book_name=book_name,book_title=book_title,book_thought=book_thought,book_thought_author=book_thought_author,book_id=int(book_id))
    return render(request, 'books/book_thoughts.html', locals())


# 查看读书感悟
def view_book_thoughts(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    bookthoughtsList = BookThoughts.objects.filter(deleted=0)
    return render(request, 'books/view_book_thoughts.html', locals())


# 查看读书感悟详情
def view_book_thoughts_detail(request, bookthoughtsid):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    bookthoughtsDetail = BookThoughts.objects.filter(id=bookthoughtsid)[0]
    bookthoughtreplyList = BookThoughtsReply.objects.filter(deleted=0).order_by("-id")
    return render(request, 'books/book_thoughts_detail.html', locals())


# 添加读书感悟留言
@csrf_exempt
def add_book_thoughts_reply(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    bookthoughtsid = request.POST.get("bookthoughtsid", "")
    b_replycontent = request.POST.get("b_replycontent", "")
    book_thought_reply_author = request.session.get("user_name")
    if BookThoughtsReply.objects.create(book_thought_reply=b_replycontent,book_thought_reply_author=book_thought_reply_author,book_thought_id=bookthoughtsid):
        return HttpResponse(1)
    else:
        return HttpResponse(0)


# 删除读书感悟
def delete_book_thoughts(request, deleteId):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    if BookThoughts.objects.filter(id=deleteId).update(deleted=1):
        return HttpResponse(1)
    else:
        return HttpResponse(0)

# 更新心愿书点赞数量
@csrf_exempt
def updataWishAgreeCount(request):
    if request.session.get('is_login', None) is None:
        return redirect("/userlogin/index/")
    wishBookId = request.POST.get("wishBookId", "")
    agreeCount = request.POST.get("agreeCount", "")
    agreeer = request.session.get("user_name")
    agreeRecordList = AgreeRecord.objects.filter(agree_person=agreeer, wish_id_id=wishBookId)
    if (agreeRecordList.count() > 0):
        return HttpResponse(3)
    if (AgreeRecord.objects.create(agree_person=agreeer, wish_id_id=wishBookId)):
        WishBook.objects.filter(id=wishBookId).update(agree_count=agreeCount)
        return HttpResponse(1)
    return HttpResponse(0)