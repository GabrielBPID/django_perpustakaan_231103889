# Generated by Django 5.1.4 on 2024-12-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penulis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='kode_penulis',
            field=models.CharField(max_length=4),
        ),
    ]
