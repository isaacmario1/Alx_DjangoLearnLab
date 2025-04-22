# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Document, Book
from .forms import BookForm


@permission_required('bookshelf.can_view', raise_exception=True)
def view_documents(request):
    documents = Document.objects.all()
    return render(request, 'bookshelf/view_documents.html', {'documents': documents})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_document(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Document.objects.create(title=title, content=content)
        return redirect('view_documents')
    return render(request, 'bookshelf/create_document.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    if request.method == 'POST':
        document.title = request.POST.get('title')
        document.content = request.POST.get('content')
        document.save()
        return redirect('view_documents')
    return render(request, 'bookshelf/edit_document.html', {'document': document})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    if request.method == 'POST':
        document.delete()
        return redirect('view_documents')
    return render(request, 'bookshelf/delete_document.html', {'document': document})


@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
