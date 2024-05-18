from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.first_name


class Student(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(null=True, max_length=10)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name
