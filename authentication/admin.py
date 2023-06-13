from django.contrib import admin
from .models import Author, Book, Borrower, BorrowedBook

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(BorrowedBook)