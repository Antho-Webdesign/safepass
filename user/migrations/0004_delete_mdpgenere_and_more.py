# Generated by Django 4.1.3 on 2022-11-04 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_profile_password_profile_passwords'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MdpGenere',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='passwords',
            new_name='password_list',
        ),
    ]
