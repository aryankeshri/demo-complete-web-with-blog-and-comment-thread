# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .models import SignUp
from .forms import ContactForm, SignUpForm


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = 'new deafult name'
        instance.full_name = full_name
        instance.save()
        context = {
            'title': "Thank you"
        }

    # return render(request, "home.html", context)
    return render(request, "home.html", context)
    # return render(request, "example_fluid.html", context)

def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'aryankeshri@greytip.com']
        contact_message = " %s: %s via %s " % (form_full_name, form_message, form_email)
        some_html_message = """ <h1> Hello </h1>"""
        send_mail(subject, contact_message, from_email, to_email, html_message=some_html_message, fail_silently=False)

        print(form.cleaned_data)

    context = {
        'title': title,
        'form': form,
        'title_align_center': title_align_center,
    }
    return render(request, "contact.html", context)

def about(request):
    return render(request, "about.html", {})

def support(request):
    return render(request, "support.html", {})


