from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Student(models.Model):
    id_number = models.IntegerField(primary_key = True)
    full_name = models.TextField()
    committee = models.TextField()
    position = models.TextField()
    attendance = models.BooleanField()
    
    def __str__(self):
        return self.full_name
    


     
