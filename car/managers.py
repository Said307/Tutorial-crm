from django.db import models


class CarQuerySet(models.QuerySet):
    def mn(self):
        return self.filter(modelname__contains="i")

    def mf(self):
        return self.filter(manufacturer="A")
 



class BMWManager(models.Manager):

    # Override manager's base queryset
    #def get_queryset(self):
        #return super().get_queryset().filter(manufacturer_id__name="BMW")
    
    # Create custom manager metrhods, based on get_queryset()
    def a_cars(self):
        return self.filter(modelname__contains="3")
    
    

    def get_queryset(self):
        return CarQuerySet(self.model, using=self._db)
    


    def mn(self):
        return self.get_queryset().mn()

    def mf(self):
        return self.get_queryset().mf() 