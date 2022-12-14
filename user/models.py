from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from generator.models import GenPass

user = get_user_model()


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # password_list = models.OneToOneField(GenPass, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', )
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['user']

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
