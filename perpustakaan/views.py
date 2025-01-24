from django.shortcuts import render

def index(request):
    context = {
        'title' : '231103889',
    }
    return render(request, 'perpustakaan.html', context)