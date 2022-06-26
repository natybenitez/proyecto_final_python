from django.db import models
#from slugify import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Blog application imports.
from books.models import Category
#from blog.utils.blog_utils import count_words, read_time

# Third party app imports
from ckeditor_uploader.fields import RichTextUploadingField
#from taggit.managers import TaggableManager

class Posts(models.Model):

    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='articles')
    title = models.CharField(max_length=200, null=False, blank=False)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    body = RichTextUploadingField(blank=True)

    #tags = TaggableManager(blank=True)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    count_words = models.CharField(max_length=50, default=0)
    read_time = models.CharField(max_length=50, default=0)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

    '''def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.count_words = count_words(self.body)
        self.read_time = read_time(self.body)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'username': self.author.username.lower(), 'slug': self.slug})'''

