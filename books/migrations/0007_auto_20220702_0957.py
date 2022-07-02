# Generated by Django 3.2.13 on 2022-07-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_rename_nombre_writer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='web_url',
            field=models.URLField(blank=True, verbose_name='Web Oficial'),
        ),
        migrations.AlterUniqueTogether(
            name='writer',
            unique_together={('name', 'lastname')},
        ),
    ]
