from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_category'
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = ('name', 'description')
        indexes = [
            models.Index(fields=['name', 'description']),
        ]

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('archived', 'Archived'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True ,related_name='posts')
    featured_image = models.ImageField(default='fallback.png', blank=True )
    thumbnail = models.ImageField(default='fallback_thumbnail.png', blank=True )
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.staus = 'published'
        self.save()

    def clean_title(self):
        return self.title.strip().capitalize()
    
    class Meta:
        db_table = 'blog_post'
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        unique_together = ('title', 'content')
        indexes = [
            models.Index(fields=['title', 'content']),
        ]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'

    class Meta:
        db_table = 'blog_comment'
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        indexes = [
            models.Index(fields=['name', 'email']),
        ]