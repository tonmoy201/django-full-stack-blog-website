# Generated by Django 3.2.9 on 2021-11-30 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='picture',
            new_name='profile_picture',
        ),
    ]