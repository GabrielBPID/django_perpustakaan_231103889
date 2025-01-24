from django.shortcuts import render, redirect 
from .models import Book
from django.http import HttpResponse

def index(request):
    buku = Book.objects.all()
    context ={
        'Title' : 'Perpustakaan STMIK Pontianak',
        'Heading' : 'Daftar Buku Ilmu Komputer',
        'Buku' : buku,
    }
    return render(request, 'buku.html', context)

def bukuadd(request):
    context ={
        'Title' : 'Perpustakaan STMIK Pontianak',
        'Heading' : 'Form Pengisian Data Buku',
    }
    return render(request, 'bukuadd.html', context)

def process_bukuadd(request):
    if request.method == 'POST':
        kode_buku =request.POST.get('kode_buku')
        judul_buku = request.POST.get('judul_buku')
        pengarang = request.POST.get('pengarang')
        penerbit = request.POST.get('penerbit')
        tahun = request.POST.get('tahun')
        
        buku = Book(kode_buku)
        return redirect('../../buku/')
    else:
        return HttpResponse('Invalid request method')