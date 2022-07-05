from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):

    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    title = models.CharField(max_length=200, null=False, blank=False)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    body = RichTextUploadingField(blank=True)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_published',)
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

    def __str__(self):
        return "%s %s" % (self.title, self.author)

class Podcast(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='nombre')
    writer = models.ForeignKey('books.Writer', on_delete=models.CASCADE, related_name='podcast', default=None)
    iframe = models.CharField(max_length=1000,null=False, blank=False)

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
        return "%s %s" % (self.name)