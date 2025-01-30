from django.db import models
class images(models.Model):
    photo= models.ImageField(upload_to=".myimage/")
    bprice=models.IntegerField()
    bvar=models.CharField(max_length=5)
    hprice=models.IntegerField()
    hvar=models.CharField(max_length=5)
    brand=models.CharField(max_length=30)

