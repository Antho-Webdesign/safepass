from django import forms
from django.forms import ModelForm

from contact.models import Contact


class ContactForm(ModelForm, forms.Form):
    class Meta:
        model = Contact
        fields = ['email', 'sujet', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'sujet': forms.TextInput(attrs={'placeholder': 'Sujet', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['sujet'].label = ''
        self.fields['message'].label = ''

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if not email and not sujet and not message:
            raise forms.ValidationError('Veuillez remplir tous les champs')
        return cleaned_data
