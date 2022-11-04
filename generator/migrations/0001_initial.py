# Generated by Django 4.1.3 on 2022-11-04 23:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('passwords', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Password',
                'verbose_name_plural': 'Passwords',
                'ordering': ['site'],
            },
        ),
    ]
