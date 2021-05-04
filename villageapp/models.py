from django.db import models

# Create your models here.
class Panchayath(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employees(models.Model):
    # Panchayath = models.ForeignKey(Panchayath,on_delete=models.CASCADE,related_name = "Employees")
    name = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name