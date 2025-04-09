from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello_blog, name='hello_blog'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('posts/<int:post_id>/', views.get_post_detail, name='post_detail'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug:slug>/update/', views.post_update, name='post_update'),
    path('posts/<slug:slug>/delete/', views.post_delete, name='post_delete'),

    

]
