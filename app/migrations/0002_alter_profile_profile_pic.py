# Generated by Django 4.1.7 on 2023-05-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_Pic',
            field=models.ImageField(upload_to='PP'),
        ),
    ]
