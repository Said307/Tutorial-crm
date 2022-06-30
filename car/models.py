from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

colours = (
    ("c1","Blue"),("c2","Red"),
    ("c4","Orange"),("c3","Green"),
    )
body_type = (
    ("Est","Estate"),("Sal","Saloon"),
    ("Hatch","HatchBack"),("Van","Van"),
    )



class Manufacturer(models.Model):

 
   name = models.CharField(max_length=50, help_text=" Name of car manufacturer")

   country = models.CharField("base country", max_length=50,help_text =" origin ")

   def __str__(self):
        return self.name

  

class Car(models.Model):

    reg = models.CharField(max_length=50, primary_key=True,help_text="registration plate number")

    manufacturer = models.CharField(max_length=50)

    model  = models.ForeignKey('CarModel',verbose_name='CarModel',on_delete=models.RESTRICT)
    
    colour  = models.CharField("car colour",max_length=1,choices=colours)

    body   =models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    year  =models.IntegerField("made in year",choices=body_type,help_text=" year of production")

    def mot_due(self):
        return self.year < 2015

    def __str__(self):
        return self.reg

class CarModel(models.Model):

    modelname = models.CharField(max_length=50,unique=True,help_text=" Name of car car model")

    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.RESTRICT,help_text=" cannot be deleted")

    def __str__(self):
        return self.modelname
 

class Supplier(models.Model):

    name =   models.CharField(max_length=50, help_text=" Name of supplier")

    country = models.CharField(max_length=50, help_text=" scountry of supplier ")

    def __str__(self):
        return self.name


class Part(models.Model):

   part_number =  models.CharField(max_length=50, primary_key=True,help_text="unique part number required")
   description = models.CharField(max_length=50, help_text="part description")
   car_model = models.ManyToManyField(CarModel)
   supplier = models.ForeignKey(Supplier,on_delete=models.SET_DEFAULT,default='none')

   def __str__(self):
        return self.part_number
    
   def multi_models(self):
        return self.car_model.count()>1







 


