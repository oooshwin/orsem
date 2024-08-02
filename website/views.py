from django.shortcuts import render
from django import forms
from .models import Student
from .forms import *
from django.views.generic.edit import UpdateView, View
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse

## Accounts
class Login(LoginView):
    template_name = 'register/login.html'

def index(request):
     return render(request, 'index.html')

def check_student(request):
     def get_absolute_url(self):
        return reverse('website:check_student')
     id_number = request.POST.get('id_number')
     if Student.objects.filter(id_number=id_number):
          student = Student.objects.get(id_number=id_number)
          return render(request, 'partials/student_info.html', {'student': student}  )
     return HttpResponse(f'<div class="card-body"> <h5 class="card-title">Student #{id_number} is not found in the database</h5> </div>')
     
          
def edit_attendance(request):
     def get_absolute_url(self):
        return reverse('website:edit_attendance')
     id_number = request.POST.get('attendance')
     print(f"VALUE: {request.POST.get('attendance')}")
     print('')
     student = Student.objects.get(id_number=id_number)
     print('student')
     if not student.attendance:
          student.attendance = True
          student.save()
     else:
          student.attendance = False
          student.save()
     
     return render(request, 'partials/student_info.html', {'student': student}  )
