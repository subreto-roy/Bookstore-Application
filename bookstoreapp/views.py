from django.shortcuts import render, redirect,get_object_or_404
from .models import Book,Cart
from .forms import BookForm
from django.shortcuts import render
from .models import Cart

def book_list(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'subpage.html', {'form': form})


def cart(request):
    cart = Cart.objects.first()  
    books = cart.books.all() if cart else []
    prices = [book.price for book in books]
    return render(request, 'cart.html', {'books': books, 'prices': prices})

