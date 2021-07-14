from __future__ import unicode_literals
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
        
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    trip = models.ForeignKey(Flight, on_delete=models.CASCADE)


    def __str__(self):
        return f"Hotel {self.name}"


class Event(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

