from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    regestration=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
                            
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    reg=models.IntegerField

    def __str__(self):
        return self.name
