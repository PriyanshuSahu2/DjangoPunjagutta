from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class StudentCard(models.Model):
    phone = models.IntegerField()
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.student.name
