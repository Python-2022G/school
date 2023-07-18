from django.db import models


class Pupil(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Contact(models.Model):
    pupil = models.OneToOneField(Pupil, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.email