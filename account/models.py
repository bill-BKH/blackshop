from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=13)
    username = models.CharField(max_length=130, unique=True)
    email_active_code = models.CharField(max_length=100)