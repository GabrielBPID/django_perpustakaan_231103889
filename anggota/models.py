from django.db import models

class Member(models.Model):
    id_anggota = models.CharField(max_length=4)
    nama_anggota = models.TextField()
    tanggal_lahir = models.TextField()
    tempat_tinggal = models.TextField
    profesi = models.TextField()
