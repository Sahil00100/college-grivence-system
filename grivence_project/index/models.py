from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    reg_no=models.CharField(max_length=10)
    student_class=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name+self.last_name  

class Grivence(models.Model):
    ACTION_=(
        ('submitted','submitted'),
        ('processing','processing'),
        ('finished','finished'),
    )
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    describe=models.TextField(max_length=1000)
    date=models.DateTimeField(auto_now=False)
    action=models.CharField(choices=ACTION_,max_length=100)
    def __str__(self):
        return str(self.name)
class Message(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=False)
    message=models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)
    