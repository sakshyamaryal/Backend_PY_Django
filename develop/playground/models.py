from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)  # Corrected typo: max_lenght -> max_length

    def __str__(self):  # Corrected method name: _str_ -> __str__
        return self.name
    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=250, choices=options, default='published')
    objects = models.Manager()  # Default manager
    postobjects = PostObjects()  # Custom manager

    published = models.DateTimeField(default=timezone.now)  # Added a 'published' field

    class Meta:
        ordering = ('-published',)

    def __str__(self):  # Corrected method name: _str_ -> __str__
        return self.title
