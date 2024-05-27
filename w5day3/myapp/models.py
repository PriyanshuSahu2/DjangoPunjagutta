from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.name

