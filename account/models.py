from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="img/", null=True, blank=True)
    bio = models.CharField(max_length=200)
    followers = models.ManyToManyField(User, related_name='following')
    created_on = models.DateTimeField(auto_now_add=True)
