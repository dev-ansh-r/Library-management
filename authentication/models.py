# models.py

from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'authentication'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'authentication'

class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books_borrowed = models.ManyToManyField(Book, through='BorrowedBook')

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'authentication'

class BorrowedBook(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} - {self.borrower}"

    class Meta:
        app_label = 'authentication'