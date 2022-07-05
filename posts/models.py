from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField

class Blog_post(models.Model):

    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='título',)
    subtitle = models.CharField(max_length=200, verbose_name='subtítulo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post', verbose_name='autor')
    body = RichTextUploadingField(blank=True, verbose_name='post',)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now, verbose_name='fecha de publucación')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT', verbose_name='estado')
    deleted = models.BooleanField(default=False, verbose_name='oculto')

    class Meta:
        ordering = ('-date_published',)
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

    def __str__(self):
        return "%s %s" % (self.title, self.author)
        

class Podcast(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='nombre')
    writer = models.ForeignKey('books.Writer', on_delete=models.CASCADE, related_name='podcast', default=None)
    iframe = models.CharField(max_length=5000,null=False, blank=False)

    class Meta:
        verbose_name = 'podcast'
        verbose_name_plural = 'podcasts'

    def __str__(self):
        return "%s %s" % (self.name, self.writer.name)

class Interview(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='nombre')
    writer = models.ForeignKey('books.Writer', on_delete=models.CASCADE, related_name='interview', default=None)
    iframe = models.CharField(max_length=1000,null=False, blank=False)

    class Meta:
        verbose_name = 'entrevista'
        verbose_name_plural = 'entrevistas'

    def __str__(self):
        return "%s" % (self.name)