# Generated by Django 4.1.3 on 2022-11-07 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generator', '0007_alter_genpass_current_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genpass',
            name='current_user',
        ),
        migrations.AddField(
            model_name='genpass',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
