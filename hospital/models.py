from django.db import models

class Hospital(models.Model):
    hospital_id=models.AutoField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=100)
    established_date=models.IntegerField()
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
