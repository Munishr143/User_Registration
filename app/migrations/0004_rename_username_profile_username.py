# Generated by Django 4.1.7 on 2023-05-02 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_username_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userName',
            new_name='username',
        ),
    ]
