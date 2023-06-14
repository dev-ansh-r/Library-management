from django.contrib.auth.models import User
from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from Library import settings
from .models import Book, Borrower, BorrowedBook
import datetime

def home(request):
    return render (request, "authentication/index.html")

def search_books(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(title__icontains=query, available=True)
    else:
        books = []

    context = {'books': books}
    return render(request, 'authentication/search_results.html',context)

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpass = request.POST.get('cpass')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists. Please!! Try someother username")

        if User.objects.filter(email=email):
            messages.info(request, "Email already exists. login or reset your password")

        if len(username) > 10:
            messages.info(request, "Username must be under 10 characters")

        if not username.isalnum():
            messages.info(request, "Username should only contain letters and numbers")

        if password != cpass:
            messages.info(request, "Passwords do not match")

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "Your account has been Suucessfully created.")
        
        return redirect('login')
    return render (request, "authentication/register.html")


def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('home')
        
    return render (request, "authentication/login.html")


def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def borrow(request):
    if request.method == 'POST':
        book_title = request.POST.get('book_id')
        username = request.POST.get('username')
        try:
            book = Book.objects.get(title=book_title)
            borrower = Borrower.objects.get(user__username=username)
        except(Book.DoesNotExist, Borrower.DoesNotExist):
            return HttpResponse("Book or User does not exist")
        
        if book.is_available:
            borrowed_book = BorrowedBook.objects.create(borrower=borrower, book=book, borrowed_date=datetime.date.today())
            borrowed_book.save()
        
        book.is_available = False
        book.save()
        return HttpResponse("Borrowed Book Successfully")
    return HttpResponse("Invalid request you dumb shit")