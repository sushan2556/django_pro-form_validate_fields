from django.db import models

# Create your models here.
class Company(models.Model):
    company_ID = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                        (('IT','IT'),
                        ('Non IT','Non IT'),
                        ('Mobile phn','Mobile phn')
                        ))
    added_date = models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + " - "+ self.location

# Create Employee APi
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
                            ('Manager','Manager'),
                            ('Software dev','Software Developer'),
                            ('Project lead','Project Lead')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
