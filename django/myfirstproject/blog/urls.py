from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello_blog, name='hello_blog'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.get_post_detail, name='post_detail'),
    path('feedback/', views.submit_feedback, name='submit_feedback')

]
