from django.db import models
from django.utils import timezone


# Create your models here.

# Create your models here.
class GenPass(models.Model):
    site = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    passwords = models.CharField(max_length=300)

    def __str__(self):
        return self.site

    class Meta:
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'
        ordering = ['site']
