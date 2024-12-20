from django.db import models

class author(models.Model):
    kode_penulis = models.TextField()
    nama_penulis = models.TextField()
    alamat_penulis = models.TextField()
    kota_penulis = models.TextField()
    telp_penulis = models.TextField()
    email_penulis = models.TextField()
    
    def __str__(self):
        return self.nama_penulis