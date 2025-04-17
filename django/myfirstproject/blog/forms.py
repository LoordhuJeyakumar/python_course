from django import forms
from .models import Post, Comment, Category

# Basic form - not tied to any model
class ContactForm(forms.Form):
    """
    A basic contact form with fields for name, email, and message.
    """
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the subject'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}))

    def clear_message(self):
        message = self.cleaned_data.get('message', '')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
    

class PostForm(forms.ModelForm):
    """
    A form for creating or updating a blog post.
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'status', 'category', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        help_texts = {
            'title': 'Enter the title of the post',
            'slug': 'Enter the slug of the post (e.g., my-post)',
            'content': 'Enter the content of the post',
            'status': 'Select the status of the post',
            'category': 'Select the category of the post',
            'published_date': 'Enter the published date of the post Leave empty for draft',
        }


class CommentForm(forms.ModelForm):
    """
    A form for creating or updating a comment on a blog post.
    """
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        labels = {
            'name': 'Name',
            'email': 'Email',
            'content': 'Your Comment',
        }

        help_texts = {
            'name': 'Enter your name',
            'email': 'Enter your email address',
            'content': 'Enter your comment',
        }


class CategoryForm(forms.ModelForm):
    """
    A form for creating or updating a category.
    """
    class Meta:
        model = Category
        fields = ['name', 'description', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Name',
            'slug': 'Slug',
            'description': 'Description',
        }

        help_texts = {
            'name': 'Enter the name of the category',
            'slug': 'Enter the slug of the category (e.g., my-category)',
            'description': 'Enter a description of the category',
        }