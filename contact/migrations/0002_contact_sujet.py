# Generated by Django 4.1.3 on 2022-11-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sujet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
