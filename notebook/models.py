from django.db import models

# Create your models here.
class UserUn(models.Model):
    firstname = models.CharField(max_length = 64)
    lastname = models.CharField(max_length = 64)
    email = models.EmailField(max_length = 64)
    password = models.CharField(max_length = 32)

    def __str__(self):
        return f"{self.firstname} {self.lastname} Email:{self.email}"
    