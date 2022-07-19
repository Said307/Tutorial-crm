from django.contrib import admin

from . models import *
from car.models import *
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["reg","year","model","colour","body","price",]


@admin.register(Part)
class CarAdmin(admin.ModelAdmin):
    list_display = ["part_number","description","multi_models","get_models","supplier"]

@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ["modelname","manufacturer","get_all_parts"]

admin.site.register(CustomUser)

#admin.site.register(Car)

#admin.site.register(CarModel)


admin.site.register(Manufacturer)


admin.site.register(Supplier)


#admin.site.register(Part)
