from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_learner = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    education_level = models.CharField(max_length=100)
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    speciality = models.CharField(max_length=100)
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)



