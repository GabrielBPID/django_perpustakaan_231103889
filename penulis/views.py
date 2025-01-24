from django.shortcuts import render

from .models import author

def index(request):
    penulis = author.objects.all()
    context ={
        'Title' : 'Penulis',
        'Heading' : 'Daftar Penulis Buku',
        'Penulis' : penulis,
    }
    return render(request, 'penulis.html', context)