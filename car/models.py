import datetime
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .managers import *
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

     

    model  = models.ForeignKey('CarModel',verbose_name='CarModel',on_delete=models.RESTRICT)
    
    colour  = models.CharField("car colour",max_length=2,choices=colours)

    body   =models.CharField(max_length=50,choices=body_type,)
    price = models.IntegerField(null=True)
    year  =models.PositiveIntegerField("made in year", help_text = " year of production",validators=[MinValueValidator(1904), MaxValueValidator(datetime.date.today().year) ])
    
   

    def mot_due(self):
        return self.year < 2015

    def __str__(self):
        return self.reg

class CarModel(models.Model):

    modelname = models.CharField(max_length=50,unique=True,help_text=" Name of car car model")

    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.RESTRICT,help_text=" cannot be deleted")
    objects = models.Manager() 
    bmw_cars = BMWManager()
   

    def __str__(self):
        return self.modelname

    def get_all_parts(self):
        return '\n, '.join([p.part_number for p in self.part_set.all()])
 

class Supplier(models.Model):

    name =   models.CharField(max_length=50, help_text=" Name of supplier")

    country = models.CharField(max_length=50, help_text=" country of supplier ")

    def __str__(self):
        return self.name


class Part(models.Model):

   part_number =  models.CharField(max_length=50, primary_key=True,help_text="unique part number required")
   description = models.CharField(max_length=50, help_text="part description")
   car_model = models.ManyToManyField(CarModel)
   supplier = models.ForeignKey(Supplier,on_delete=models.SET_DEFAULT,default='none',related_name="supplier_name")

   def __str__(self):
        return self.part_number
    
   def multi_models(self):
        return self.car_model.count()
    
   def get_models(self):
        return "\n, ".join([p.modelname for p in self.car_model.all()])







 


