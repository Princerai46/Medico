from django.db import models

class Hospital(models.Model):
    name=models.CharField(max_length=100)
    established_date=models.IntegerField(max_length=4)
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
