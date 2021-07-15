from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from datetime import datetime
from datetime import date
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def planner_view(request):
    template_name = "tripplanner/planner.html"

    return render(request, template_name, {})


def filter_flight_destination(request):
    """
    Dropdown menu filters flight's destination
    """
    try:
        selected_choice = Flights.objects.filter(airplane_from__eq=request.GET['from'])
    except (KeyError):
        return render(request, "tripplanner/planner.html",
            {"error_message": "Please select the city you are planning to travel to."})

    



class CalendarView(generic.ListView):
    model = Event
    template_name = 'tripplanner/cal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        # d = get_date(self.request.GET.get('day', None))
        d = date.today()

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context
