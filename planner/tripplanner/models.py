from __future__ import unicode_literals
import datetime
from django.urls import reverse

from django.db import models


class City(models.Model):
    """
    Cities of Australia stored in the database
    """
    name = models.CharField(max_length=200)
    # The IATA code
    code = models.CharField(max_length=3, default="")

    def __str__(self):
        return self.name


class Flight(models.Model):
    airline = models.CharField(max_length=200, default="")
    flight_no = models.CharField(max_length=200, default="")
    airport_from = models.ForeignKey(City, related_name="airport_from", on_delete=models.PROTECT, null=True)
    airport_to = models.ForeignKey(City, related_name="airport_to", on_delete=models.PROTECT, null=True)

    boarding_time = models.DateTimeField('boarding time')
    arrival_time = models.DateTimeField('arrival time')

    url = models.URLField(max_length=200, default="")

    def get_duration(self):
        """
        Returns Datetime delta object of duration
        """
        return self.arrival_time - self.boarding_time

    def __str__(self):
        return f'Flight {self.airport_from}-{self.airport_to}'


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    trip = models.ForeignKey(Flight, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return f"Hotel {self.name}"


class Event(models.Model):
    # title = models.CharField(max_length=200)
    # description = models.TextField()
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()

    title = models.CharField(max_length=200)
    # day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.DateTimeField(u'Starting time', blank=True, null=True)
    end_time = models.DateTimeField(u'Final time', blank=True, null=True)
    notes = models.TextField(u'Textual Notes', blank=True, null=True)
    
    @property
    def get_html_url(self):
        url = reverse('tripplanner:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
        
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'


class Trip(models.Model):
    """
    A trip in Australia
    """
    city_from = models.ForeignKey(City, related_name="city_from", on_delete=models.PROTECT, null=True)
    city_to = models.ForeignKey(City, related_name="city_to", on_delete=models.PROTECT, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT, null=True)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')


    def __str__(self):
        return f"Trip to {self.city}, {self.country}"