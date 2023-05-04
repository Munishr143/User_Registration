from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    Address=models.TextField()
    Profile_Pic=models.ImageField(upload_to='PP')

    def __str__(self) -> str:
        return self.username
