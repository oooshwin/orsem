from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
     class Meta:
          model = Student
          fields = ['attendance']
