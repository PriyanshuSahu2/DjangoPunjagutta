from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=25, null=True)
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=25, null=True)


    
