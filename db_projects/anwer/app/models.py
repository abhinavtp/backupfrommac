from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'profile_images' )


    class Meta():
        db_table="registration"

class product(models.Model):
    name =models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity= models.IntegerField()
    catagory = models.CharField(max_length=100)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)

    class Meta():
        db_table="product"


class Doctor(models.Model):
    name =models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    department= models.CharField(max_length=100)
    place = models.CharField(max_length=100)
     
    class Meta():
        db_table="doctor"
 


    
















