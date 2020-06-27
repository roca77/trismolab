from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Learner, Teacher, User


class LearnerSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    # This allows us to quickly save some data while the user is being created
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email_address')
        user.save()
        learner = Learner.objects.create(user=user)
        learner.save()
        return learner


class TeacherSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email_address')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.save()
        return teacher
