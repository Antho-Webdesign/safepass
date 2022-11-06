from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    sujet = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    sending_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.sending_date

    class Meta:
        ordering = ['-sending_date']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
