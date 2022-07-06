from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    relationship = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname
