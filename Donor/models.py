from django.db import models

class donor_list(models.Model):
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=100, default=None)
    phn= models.CharField(max_length=12, default=None)
    blood = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=10, default=None)

class img(models.Model):
    image =models.ImageField(upload_to='img')