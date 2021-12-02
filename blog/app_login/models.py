from django.db import models
from django.contrib.auth.models import User


class NewUser(models.Model):
    user=models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="profile_picture",null=True,blank=True)