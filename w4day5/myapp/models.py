from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    age = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def fullName(self):
        return f'{self.first_name} {self.last_name}'
        
        


class Book(models.Model):
    book_name = models.CharField(max_length=30, null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return self.book_name
