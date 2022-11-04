from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from generator.models import GenPass

user = get_user_model()


class MdpGenere(models.Model):
    url_site = models.URLField(max_length=200)
    mot_de_passe = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.url_site

    class Meta:
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'
        ordering = ['-date_creation']


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passwords = models.ForeignKey(GenPass, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images',)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

# Create your models here.
