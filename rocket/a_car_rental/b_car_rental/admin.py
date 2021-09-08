from django.contrib import admin
from .models import Car, RentCar


@admin.register(Car)
class Car(admin.ModelAdmin):

    class Meta:
        model = Car


@admin.register(RentCar)
class RentCar(admin.ModelAdmin):

    class Meta:
        model = RentCar
