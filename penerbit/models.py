from django.db import models

class Penerbit(models.Model):
    kode_penerbit = models.CharField(max_length=4)
    nama_penerbit = models.TextField(max_length=20)
    alamat_penerbit = models.TextField(max_length=20)
    kota_penerbit = models.TextField(max_length=20)
    email_penerbit = models.TextField(max_length=30)
    telp_penerbit = models.TextField(max_length=12)
    def __str__(self):
        return self.nama_penerbit