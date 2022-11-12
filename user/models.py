from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

user = get_user_model()


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='/img_profil/default.jpg', upload_to='user/media/img_profil/',)
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
