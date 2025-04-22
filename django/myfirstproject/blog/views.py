from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

import os
from django.conf import settings


from django.http import JsonResponse
from django.views.generic import ListView
import json

from .models import Post, Category, Comment

from .forms import CommentForm, PostForm, CategoryForm, ContactForm
from django.contrib import messages

# Create your views here.

def hello_blog(request):
    return HttpResponse("Hello from the blog app!")


#URLs Routing 
#Sample blog data

posts = [
    {
        'id':1 ,
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'id':2 ,
        'author': 'Jane Doe',   
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'id':3  ,
        'author': 'John Doe',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 29, 2018'
    }
    
]

# def post_list(request):
#     context = {
#         'posts': posts
#     }
#     # send posts as JSON

#     return JsonResponse(context)


def get_post_detail(request, post_id):
    post = next(post for post in posts if post['id'] == post_id)
    return JsonResponse(post)


#Re-path example

regex = r'^post/(?P<post_id>\d+)/$' 
# Explanation: The regex pattern starts with 'post/' followed by a capturing group named 'post_id' that matches one or more digits (\d+). The '$' at the end indicates the end of the URL pattern.

#Get and POST requests in single view


def submit_feedback(request):
    if request.method == 'POST':
        # Process the form data here (e.g., save feedback to a database)
        feedback = request.POST.get('feedback', 'No feedback received')
        return HttpResponse(f"Thank you for your feedback: {feedback}")
    else:  # request.method == 'GET'
        # Display the HTML form on a GET request
        form_html = """
        <h2>Feedback Form</h2>
        <form method="post">
            {% csrf_token %}
            <input type="text" name="feedback" placeholder="Enter your feedback">
            <button type="submit">Submit Feedback</button>
        </form>
        """
        return HttpResponse(form_html)
    

def load_posts():
    """
        Utility function to load posts from the JSON file.
        Returns:
            list: A list of dictionaries representing posts.
        """
    json_file_path = os.path.join(settings.BASE_DIR, 'data\posts.json')

    with open(json_file_path, 'r') as file:
        posts = json.load(file)

        posts.sort(key=lambda x: x['published_date'], reverse=True)

        return posts


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Blog Posts'
    }
    return render(request, 'posts/post_list.html', context)


def post_create(request):
    status_choices = Post.STATUS_CHOICES
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # Set author if needed
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, "Error creating post. Please check the form.")
    else:
        form = PostForm()
    
    return render(request, 'posts/post_form.html', {'form': form, 'status_choices': status_choices})


def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, "Error updating post. Please check the form.")
    else:
        form = PostForm(instance=post)
    
    return render(request, 'posts/post_form.html', {'form': form, 'post': post})

def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        # Delete the image files if they exist and aren't the default
        if post.featured_image and post.featured_image.name != 'fallback.png':
            if os.path.isfile(post.featured_image.path):
                os.remove(post.featured_image.path)
        
        if post.thumbnail and post.thumbnail.name != 'fallback.png':
            if os.path.isfile(post.thumbnail.path):
                os.remove(post.thumbnail.path)
                
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('post_list')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})


# Basic Form -  Contact
def contact_view(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here (e.g., send an email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # For demonstration purposes, let's print the form data
            print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")

            # Redirect to a success page or do something else
            return redirect('success_page')  # Replace 'success_page' with your actual success page URL
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})


# ModelForm - Create Post
def post_create_form(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, 'Post created successfully.')

            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, 'Error creating post. Please check the form.')
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', {'form': form, 'title': 'Create New Post'})



# ModelForm - Edit Post
def post_update_form(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, 'Error updating post. Please check the form.')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form, 'title': f'Edit Post: {post.title}'})


# Comment Form - Create Comment on post detail page
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


def catagory_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully.')
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'posts/category_form.html', {'form': form, 'title': 'Create New Category'})