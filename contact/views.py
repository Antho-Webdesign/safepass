from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact-success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact-view.html', context)


def success_view(request):
    return HttpResponse("Success! Merci pour votre message.")
