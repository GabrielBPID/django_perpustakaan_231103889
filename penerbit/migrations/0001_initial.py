# Generated by Django 5.1.4 on 2024-12-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penerbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_penerbit', models.CharField(max_length=4)),
                ('nama_penerbit', models.TextField(max_length=20)),
                ('alamat_penerbit', models.TextField(max_length=20)),
                ('kota_penerbit', models.TextField(max_length=20)),
                ('email_penerbit', models.CharField(max_length=30)),
                ('telp_penerbit', models.CharField(max_length=12)),
            ],
        ),
    ]