# Generated by Django 3.2.13 on 2022-06-28 02:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_writer_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Agrega información sobre este/a autor/a'),
        ),
    ]