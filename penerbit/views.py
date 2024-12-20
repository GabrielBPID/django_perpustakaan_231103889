from django.shortcuts import render

from .models import Penerbit

def index(request):
    penerbit = Penerbit.objects.all()
    context ={
        'TItle' : 'Penerbit',
        'Heading' : 'Daftar Penerbit Buku',
        'Penerbit' : penerbit,
    }
    return render(request, 'penerbit/index.html', context)