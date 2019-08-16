from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from .models import Books, Authors

def index(request):
    all_the_books={
        "all_the_books1": Books.objects.all()
    }
    
    return render(request, "books/index.html", all_the_books)

#BOOK FUNCTIONS

#book info page
def book_view(request, book_id):
    context = {
        'books' : Books.objects.get(id = book_id),
        'authors' : Books.objects.get(id = book_id).Authors.all(),
        'all_authors' : Authors.objects.all(),
    }
    return render(request, "books/books_view.html", context)

#book page - add author
def append_authors(request, book_id):
    if request.method=="POST":
        thisBook = Books.objects.get(id=book_id)
        thisAuthor = Authors.objects.get(id=request.POST['author_id'])
        thisBook.Authors.add(thisAuthor)
    return redirect("/books/"+book_id)

#add book    
def add_book(request):
    print ("I am before the if")
    if request.method=="POST":
        Books.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect("/")



#AUTHORS FUNCTIONS

#all author page
def author(request):
    data = {
        "all_authors": Authors.objects.all()
    }
    return render(request, "books/authors.html", data)

#Add Author to Author Page
def add_author(request):
    print ("I am before the if")
    if request.method=="POST":
        Authors.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect("/authors")

#Add books to authors**********
def append_books(request, author_id):
    thisBook = Books.objects.get(id=request.POST['book_id'])
    thisAuthor = Authors.objects.get(id=author_id)
    thisAuthor.books.add(thisBook)
    return redirect(f'/authors/{author_id}')

#author info page - by ID
def author_view(request, author_id):
    context = {
        'books' : Authors.objects.get(id = author_id).books.all(),
        'authors' : Authors.objects.get(id = author_id),
        'all_authors' : Authors.objects.all(),
        'other_books' : Books.objects.exclude(Authors__id=author_id)
    }
    return render(request, "books/authors_view.html", context)