from django.db import models

# Create your models here.
# dog model with name, breed, color and gender
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
# account model that includes user name, real name, account number , and balance
class Account(models.Model):
    userName = models.CharField(max_length=100)
    realName = models.CharField(max_length=100)
    accountNumber = models.IntegerField()
    balance = models.DecimalField(decimal_places=5, max_digits=100000)