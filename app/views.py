from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Other CRUD views: book_detail, book_create, book_update, book_delete
#create
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        print(f'Title: {title}, Author: {author}, Description: {description}')
        book = Book.objects.create(title=title, author=author, description=description)
        print(f'Book created: {book}')
        #return redirect(reverse('app:book_list'))
        return redirect('book_list')
    return render(request, 'book_form.html')

#update
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        book.title = title
        book.author = author
        book.description = description
        book.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'book': book})

#delete
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})