from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

user = get_user_model()


# Create your models here.
def get_absolute_url():
    return reverse('contact:contact-view')


class Contact(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    sujet = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    sending_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-sending_date']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('current_user', 'email', 'sujet', 'message', 'sending_date')
    list_filter = ('current_user', 'email', 'sujet', 'message', 'sending_date')
    search_fields = ('current_user', 'email', 'sujet', 'message', 'sending_date')
    ordering = ('-sending_date',)
    list_per_page = 25
