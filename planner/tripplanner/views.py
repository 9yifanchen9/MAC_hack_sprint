from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from .models import *


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

    



