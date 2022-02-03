from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media')
    Posted_on=models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ImageField(upload_to='profiles')