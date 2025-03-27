from django.shortcuts import render
from django.http import HttpResponse

import os
from django.conf import settings


from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic import ListView
import json


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
    """
        View function to display a list of blog posts.
        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            HttpResponse: The rendered HTML response with the list of posts.
        """
    posts = load_posts()

    context = {
        'posts': posts,
        'title': 'Blog Posts'
    }

    return render(request, 'posts/post_list.html', context)