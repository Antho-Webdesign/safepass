from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

import user.models
from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            current_user = request.user
            email = form.cleaned_data.get('email')
            sujet = form.cleaned_data.get('sujet')
            message = form.cleaned_data.get('message')
            contact = Contact.objects.create(current_user=current_user, email=email, sujet=sujet, message=message)
            contact.save()
            messages.success(request, 'Votre message a bien été envoyé')
            print(contact, current_user, email, sujet, message)
            return redirect('success')
        else:
            messages.error(request, 'Veuillez remplir tous les champs')
    else:
        form = ContactForm()
    context = {
        'forms': form,
    }

    return render(request, 'contact/contact-view.html', context)


def success_view(request):
    return HttpResponse("Success! Merci pour votre message.")


def delete_message(request, id):
    message = Contact.objects.get(id=id)
    message.delete()
    return redirect('contact:contact-view')


def delete_all_messages(request):
    messages = Contact.objects.all()
    messages.delete()
    return redirect('contact:contact-view')

