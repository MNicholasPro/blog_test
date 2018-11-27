# -*- coding: utf-8 -*-

from django.contrib import admin
# Register your models here.
from booksdata.models.author import Author
from booksdata.models.book import Book
from booksdata.models.booktype import Booktype
from booksdata.models.borrow_log import BorrowLog
from booksdata.models.department import Department
from booksdata.models.publisher import Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Booktype)
admin.site.register(Department)
admin.site.register(Publisher)
admin.site.register(BorrowLog)