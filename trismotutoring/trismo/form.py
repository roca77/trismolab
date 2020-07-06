from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Learner, Teacher, User, Profile


class LearnerSignUpForm(UserCreationForm):
    email_address = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    # This allows us to quickly save some data while the user is being created
    def save(self):
        user = super().save(commit=False)
        user.is_learner = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email_address')
        user.save()
        learner = Learner.objects.create(user=user)
        learner.save()
        return learner


class TeacherSignUpForm(UserCreationForm):
    email_address = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email_address')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.save()
        return teacher


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name',
                  'last_name',
                  'email',
                  'confirm_email',
                  'date_of_birth',
                  'bio',
                  'avatar'
                  ]

    def clean(self):
        """Checks if email1 and email2 are the same"""
        cleaned_data = super().clean()
        email = cleaned_data['email']
        confirm = cleaned_data['confirm_email']
        if email != confirm:
            raise forms.ValidationError("you need to enter the same email in both fields")