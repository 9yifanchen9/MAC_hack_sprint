import datetime

from django.db import models


class Trip(models.Model):
    """
    A trip in Australia
    """
    dest_city = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')


    def __str__(self):
        return f"Trip to {self.city}, {self.country}"


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_lenght=200)
    trip = models.ForeignKey(Flight, on_delete=models.CASCADE)


    def __str__(self):
        return f"Hotel {self.name}"


class Flight(models.Model):
    airline = models.CharField(max_length=200)
    airport_from = models.CharField(max_length=3)
    airport_to = models.CharField(max_length=3)

    boarding_time = models.DateTimeField('boarding time')
    arrival_time = models.DateTimeField('arrival time')


    def get_duration(self):
        """
        Returns Datetime delta object of duration
        """
        return arrival_time - boarding_time

    def __str__(self):
        return f'Flight {airport_from}-{airport_to}'

