# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .models import Document

@login_required
@permission_required('core_app.can_view', raise_exception=True)
def view_documents(request):
    docs = Document.objects.all()
    return render(request, 'core_app/view_documents.html', {'documents': docs})

@login_required
@permission_required('core_app.can_create', raise_exception=True)
def create_document(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Document.objects.create(title=title, content=content)
    return render(request, 'core_app/create_document.html')

@login_required
@permission_required('core_app.can_edit', raise_exception=True)
def edit_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    if request.method == 'POST':
        doc.title = request.POST.get('title')
        doc.content = request.POST.get('content')
        doc.save()
    return render(request, 'core_app/edit_document.html', {'document': doc})

@login_required
@permission_required('core_app.can_delete', raise_exception=True)
def delete_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    if request.method == 'POST':
        doc.delete()
    return render(request, 'core_app/delete_document.html', {'document': doc})
