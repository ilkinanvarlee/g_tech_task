from . forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings


def index_view(request):
    return render(request, 'web/index.html')


def contact_view(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = f'Name: {name}, Surname: {surname}, Email: {email}, Phone: {phone}, Message: {message}'

        send_mail(
            "You have a message from your site",
            data,
            settings.EMAIL_HOST_USER,
            ['ilkine2191@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent!')
        return redirect(request.META['HTTP_REFERER'])

    context = {'form': form}

    return render(request, "web/contact.html", context=context)

