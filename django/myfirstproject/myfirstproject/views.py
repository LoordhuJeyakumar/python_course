from django.shortcuts import render, redirect
from  blog.forms import ContactForm
import random
import string
from django.contrib import messages

def homepage(request):

    

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')


def generate_refrence_number():
    """Generate a random reference number for the contact form submission."""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(10)) # 10 characters


def contact(request):
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

            reference_number = generate_refrence_number()
            print(f"Reference Number: {reference_number}")

            request.session['reference_number'] = reference_number

            messages.success(request, f"Your message has been sent. Reference Number: {reference_number}")

            # Redirect to a success page or do something else
            return redirect('success_page') 
        else:
            #handle form errors
            messages.error(request, 'Please correct the errors in the form.')

        # return render(request, 'success_page.html', {'reference_number': reference_number})
    else:
        # This is a GET request, display the initial form
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_page(request):
    reference_number = request.session.get('reference_number')

    if 'reference_number' in request.session:
        del request.session['reference_number'] 

    return render(request, 'success_page.html', {'reference_number': reference_number})