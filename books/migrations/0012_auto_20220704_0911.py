# Generated by Django 3.2.13 on 2022-07-04 12:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_rename_book_name_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=ckeditor.fields.RichTextField(default='', verbose_name='resumen'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=500, verbose_name='título'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_published',
            field=models.IntegerField(verbose_name='año de publicación'),
        ),
    ]
