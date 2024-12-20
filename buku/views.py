from django.shortcuts import render
from .models import Book

def index(request):
    buku = buku.objects.all()
    context ={
        'Title' : 'Perpustakaan STMIK Potianak',
        'Heading' : 'Daftar Buku Ilmu Komputer',
        'Book' : buku,
    }
return render(request, 'index.html', context)