from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'blog_post'
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        unique_together = ('title', 'content')
        indexes = [
            models.Index(fields=['title', 'content']),
        ]