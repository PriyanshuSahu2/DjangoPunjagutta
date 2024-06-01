from django import forms
from django.db import models

class StudentModelForm(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()