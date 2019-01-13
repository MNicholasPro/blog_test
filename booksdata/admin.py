# -*- coding: utf-8 -*-

from django.contrib import admin
# Register your models here.
from booksdata.models.agree_record import AgreeRecord
from booksdata.models.author import Author
from booksdata.models.book import Book
from booksdata.models.book_thoughts import BookThoughts
from booksdata.models.book_thoughts_reply import BookThoughtsReply
from booksdata.models.booktype import Booktype
from booksdata.models.borrow_log import BorrowLog
from booksdata.models.department import Department
from booksdata.models.publisher import Publisher
from booksdata.models.wish_book import WishBook

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Booktype)
admin.site.register(Department)
admin.site.register(Publisher)
admin.site.register(BorrowLog)
admin.site.register(WishBook)
admin.site.register(BookThoughts)
admin.site.register(BookThoughtsReply)
admin.site.register(AgreeRecord)