from django.db import models

# Create your models here.
class test2model(models.Model):
    testid = models.IntegerField()
    name = models.CharField(max_length=120)
    salary = models.IntegerField()
    mobilenum = models.IntegerField()

class test3model(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=120)
    empsalary = models.IntegerField()
    empmob=models.IntegerField()
    