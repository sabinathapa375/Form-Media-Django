from django.db import models
from django.contrib.auth.models import AbstractUser #Importing manually for the use of the abstract user

# Create your models here.
class Registration(AbstractUser):

    phone=models.IntegerField(null=True)
    picture = models.ImageField(blank=True,null=True,upload_to="user_picture/") # For picture upload
    document = models.FileField(blank=True,null=True, upload_to="user_document/") # For document upload
    
    def __str__(self):
        return self.username

    