from django.db import models

class Book(models.Model):
    kode_buku = models.CharField(max_length=4)
    judul_buku = models.TextField()
    pengarang = models.TextField()
    penerbit = models.TextField
    tahun = models.TextField()
