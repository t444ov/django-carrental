from django.db import models
from django.utils import timezone
from django.conf import settings


import datetime
YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))
YEAR_CHOICES = list(reversed(YEAR_CHOICES))


class Car(models.Model):
    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
        db_column='id'
    )
    brand = models.CharField(
        max_length=255,
        verbose_name='Brand',
        db_column='brand'
    )
    model = models.CharField(
        max_length=255,
        verbose_name='Model',
        db_column='model'
    )
    BODY_TYPE_CHOICES = [
        ('Convertible', 'Convertible'),
        ('Coupe', 'Coupe'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
        ('Wagon', 'Wagon'),
        ('Hatchback', 'Hatchback'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    ]
    body_type = models.CharField(
        max_length=20,
        choices=BODY_TYPE_CHOICES,
        verbose_name='Body type',
        db_column='body_type'
    )
    year_of_issue = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
        verbose_name='Year of issue',
        db_column='year_of_issue'
    )
    color = models.CharField(
        max_length=255,
        verbose_name='Color',
        db_column='color'
    )
    engine_volume = models.FloatField()
    power = models.IntegerField()
    FUEL_TYPE_CHOICES = [
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Electricity', 'Electricity'),
    ]
    fuel_type = models.CharField(
        max_length=12,
        choices=FUEL_TYPE_CHOICES,
        verbose_name='Fuel type',
        db_column='fuel_type'
    )
    TRANSMISSION_TYPE_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
        ('Automated Manual', 'Automated Manual'),
        ('Continuously Variable', 'Continuously Variable'),
    ]
    transmission_type = models.CharField(
        max_length=30,
        choices=TRANSMISSION_TYPE_CHOICES,
        verbose_name='Transmission type',
        db_column='transmission_type'
    )
    CAR_DRIVE_TYPE_CHOICES = [
        ('FWD', 'FWD'),
        ('RWD', 'RWD'),
        ('AWD', 'AWD'),
        ('4WD', '4WD'),
    ]
    car_drive_type = models.CharField(
        max_length=35,
        choices=CAR_DRIVE_TYPE_CHOICES,
        verbose_name='Car drive type',
        db_column='car_drive_type'
    )
    license_plate = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='License plate',
        db_column='license_plate'
    )
    number_of_seats = models.IntegerField()
    description = models.CharField(
        max_length=255,
        verbose_name='Description',
        db_column='description'
    )
    price = models.FloatField()
    # image = models.ImageField(
    #     upload_to='img/car_image/',
    #     null=True,
    #     blank=True,
    #     verbose_name='Image',
    #     db_column='image'
    # )
    CAR_STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Rented', 'Rented'),
        ('Maintenance', 'Maintenance'),
    ]
    car_status = models.CharField(
        max_length=12,
        choices=CAR_STATUS_CHOICES,
        default='Available',
        verbose_name='Car status',
        db_column='car_status'
    )
    publishing_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Publishing date',
        db_column='publishing_date'
    )
    published_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Published by',
        db_column='published_by'
    )

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'Cars'
        db_table = 'cars'

    def __str__(self):
        return f'{self.brand} {self.model} : {self.license_plate}'


class RentCar(models.Model):
    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
        db_column='id'
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Client',
        db_column='client'
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Car',
        db_column='car'
    )
    booking_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Booking date',
        db_column='booking_date'
    )
    date_of_issue = models.DateTimeField(
        verbose_name='Date of issue',
        db_column='date_of_issue'
    )
    planned_return_date = models.DateTimeField(
        verbose_name='Planned return date',
        db_column='planned_return_date'
    )
    total_days = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Total days',
        db_column='total_days'
    )
    is_bill_paid = models.BooleanField(
        default=False,
        verbose_name='is bill paid',
        db_column='is_bill_paid'
    )
    return_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Return date',
        db_column='return_date'
    )
    total_payment_amount = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Total payment amount',
        db_column='total_payment_amount'
    )
    request_responded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='workers',
        verbose_name='Request responded by',
        db_column='request_responded_by'
    )
    REQUEST_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    ]
    request_status = models.CharField(
        max_length=30,
        choices=REQUEST_STATUS_CHOICES,
        default="Pending",
        verbose_name='Request status',
        db_column='request_status'
    )

    class Meta:
        verbose_name = 'rent car'
        verbose_name_plural = 'Rent cars'
        db_table = 'rent_cars'

    def __str__(self):
        return f'{self.client} : {self.car}'
