from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state = models.CharField(max_length=30,  null=True)
    country = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=40, null=True)
    profile_pic = models.FileField(verbose_name="Profile Picture", null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=30, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publishers = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'
