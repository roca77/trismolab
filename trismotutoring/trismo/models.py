from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import User


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
    last_login = models.DateTimeField(default=timezone.now)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    speciality = models.CharField(max_length=100)
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    last_login = models.DateTimeField(default=timezone.now)


class Profile(models.Model):
    # if the user is the deleted the profile will be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default="")
    confirm_email = models.EmailField(default="")
    first_name = models.CharField(default="", max_length=250)
    last_name = models.CharField(default="", max_length=250)
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(validators=[validators.MinLengthValidator(10)])
    avatar = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        """Prints username from database as string"""
        return f'{self.user.username} Profile'



