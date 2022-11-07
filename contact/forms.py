from django import forms
from django.urls import reverse


def get_absolute_url():
    return reverse('contact-view')


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-sending_date']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
