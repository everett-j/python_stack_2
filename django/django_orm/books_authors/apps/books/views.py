from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from .models import Books, Authors

def index(request):
    all_the_books={
        "all_the_books1": Books.objects.all()
    }
    
    return render(request, "books/index.html", all_the_books)



def book_view(request, book_id):
    
    context = {
        'books' : Books.objects.get(id = book_id),
        'authors' : Books.objects.get(id = book_id).Authors.all(),
        'all_authors' : Authors.objects.all(),
    }
    return render(request, "books/books_view.html", context)

def author_view(request, author_id):
    option = Books.objects.get(id = request.POST['select_book'])
    Authors.objects.get(id = author_id).books.add(option)
    return redirect(f'/author_info/{author_id}')

def author(request, author_id):
    context = {
        'authors' : Authors.objects.get(id = author_id),
        'books' : Authors.objects.get(id = author_id).books.all(),
        'all_books' : Books.objects.all(),
    }
    return render(request, "books/authors.html", context)

def add_author(request, new_author):
    new_author = Authors.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'])
    return redirect('books/authors.html')

def append_authors(request, book_id):
    option = Authors.objects.get(id = request.POST['select_author'])
    Books.objects.get(id = book_id).authors.add(option)
    return redirect(f'books/books_view.html/{book_id}')

def add_book(request, new_book):
    new_book = Books.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def append_books(request, author_id, select_book):
    option = Books.objects.get(id = request.POST['select_book'])
    Authors.objects.get(id = author_id).books.add(option)
    return redirect(f'/author_info/{author_id}')