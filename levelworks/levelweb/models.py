from django.db import models

# Create your models here.


class Student(models.Model):

    # Child's details
    c_fname = models.CharField(max_length=100)
    c_lname = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    term = models.IntegerField()
    
    # Parent's details
    p_fname = models.CharField(max_length=100)
    p_lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    heard_from = models.CharField(max_length=100)

    


    


