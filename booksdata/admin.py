# -*- coding: utf-8 -*-

from django.contrib import admin
# Register your models here.
from booksdata.models import author, book, booktype, department, publisher

admin.site.register(author.Author)
admin.site.register(book.Book)
admin.site.register(booktype.Booktype)
admin.site.register(department.Department)
admin.site.register(publisher.Publisher)