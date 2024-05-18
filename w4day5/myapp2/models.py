from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Contact(models.Model):
    phone = models.IntegerField()
    city = models.CharField(max_length=30)
    student = models.OneToOneField(
        Student, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student.full_name}  {self.phone}"
