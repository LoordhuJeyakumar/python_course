# Create a management command or script to populate your database with sample data
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Post, Comment
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populates the database with sample blog data'
    
    def handle(self, *args, **options):
        # Create users
        users = []
        for i in range(5):
            username = f"user{i+1}"
            try:
                user = User.objects.create_user(
                    username=username,
                    email=f"{username}@example.com",
                    password="password123"
                )
                users.append(user)
                self.stdout.write(f"Created user: {username}")
            except:
                users.append(User.objects.get(username=username))
        
        # Create categories
        categories = []
        category_data = [
            {"name": "Python", "slug": "python", "description": "All about Python programming"},
            {"name": "Django", "slug": "django", "description": "Django web framework tutorials"},
            {"name": "JavaScript", "slug": "javascript", "description": "JavaScript tips and tricks"},
            {"name": "CSS", "slug": "css", "description": "Styling your web applications"},
            {"name": "Drafts", "slug": "drafts", "description": "Work in progress"}
        ]
        
        for cat in category_data:
            category, created = Category.objects.get_or_create(**cat)
            categories.append(category)
            if created:
                self.stdout.write(f"Created category: {category.name}")
        
        # Create posts
        status_options = ['draft', 'published', 'archived']
        post_count = 0
        
        for i in range(30):
            user = random.choice(users)
            category = random.choice(categories)
            status = random.choice(status_options)
            created_days_ago = random.randint(1, 365)
            created_date = timezone.now() - timedelta(days=created_days_ago)
            
            published_date = None
            if status == 'published':
                published_days_ago = random.randint(0, created_days_ago)
                published_date = timezone.now() - timedelta(days=published_days_ago)
            
            post, created = Post.objects.get_or_create(
                title=f"Sample Post {i+1} about {category.name}",
                slug=f"sample-post-{i+1}-about-{category.slug}",
                defaults={
                    'author': user,
                    'category': category,
                    'content': f"This is sample content for post {i+1} about {category.name}. " * 5,
                    'status': status,
                    'created_at': created_date,
                    'published_date': published_date
                }
            )
            
            if created:
                post.created_at = created_date
                if published_date:
                    post.published_date = published_date
                post.save()
                post_count += 1
                
                # Create comments for this post
                comment_count = random.randint(0, 10)
                for j in range(comment_count):
                    Comment.objects.create(
                        post=post,
                        name=f"Commenter {j+1}",
                        email=f"commenter{j+1}@example.com",
                        content=f"This is comment {j+1} on this post. Great article!" * 2
                    )
        
        self.stdout.write(f"Created {post_count} new posts with comments")