# Generated by Django 3.2.13 on 2022-07-04 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20220704_0911'),
        ('posts', '0002_remove_podcast_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='writer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='podcast', to='books.writer'),
        ),
    ]
