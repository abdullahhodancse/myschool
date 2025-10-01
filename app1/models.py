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




class Subscription(models.Model):
    SUBSCRIPTION_TYPES = [
        ('business', 'Business'),
        ('premium', 'Premium'),
        ('gold', 'Gold'),
        ('free','Free'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    type = models.CharField(max_length=20, choices=SUBSCRIPTION_TYPES, default='business')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.type}"

