from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    zip = models.IntegerField()
    def __str__(self):
        return self.email
class Employee(models.Model):
    emp_email = models.EmailField(max_length=200)
    epassword = models.CharField(max_length=200)
    eaddress = models.CharField(max_length=200)
    ecity = models.CharField(max_length = 200)
    ezip = models.IntegerField()
    def __str__(self):
        return self.emp_email