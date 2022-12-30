from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class Informations(models.Model):
    who = models.OneToOneField(User, on_delete = models.CASCADE, null=True) # one to one relation with user
    birth = models.DateField(null=True)
    gender = models.CharField(max_length=25, null=True)
    origin =  models.CharField(max_length=25, null=True)
    image = models.ImageField(upload_to="images/", null=True) #image field with path to upload
    bio = models.CharField(max_length=254, null=True) 
    joined = models.DateTimeField(auto_now_add=True) # auto now add true adds the date of the creation of the account

class Thread(models.Model):
    madeby = models.ForeignKey(User, on_delete=models.CASCADE) # one to many relation with user
    thread_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField() # textfield instead of charfield because there is no limitation of 254 chars
    photo = models.CharField(max_length=254, null=True)
    closed = models.BooleanField(default=False) # True or false 

class Post(models.Model):
    madeby = models.ForeignKey(User, on_delete=models.CASCADE)
    post_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    onwhat = models.ForeignKey(Thread, on_delete=models.CASCADE)
    who = models.ForeignKey(Informations, on_delete=models.CASCADE) 
   