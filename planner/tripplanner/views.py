from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from datetime import datetime, date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
import calendar
import pytz

from .forms import EventForm
from .models import *
from .utils import Calendar


def home_view(request, *args, **kwargs):
    return render(request, "tripplanner/index.html", {})


class PlannerView(generic.ListView):
    model = City
    template_name = "tripplanner/planner.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all cities
        context['cities'] = City.objects.all().order_by('name')

        return context


class TripView(generic.DetailView):
    model = Trip
    template_name = "tripplanner/trip.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class CalendarView(generic.ListView):
    model = Event
    template_name = 'tripplanner/cal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tripplanner:calendar'))
    return render(request, 'tripplanner/event.html', {'form': form})

def filter_flight_destination(request):
    """
    Dropdown menu filters flight's destination
    """
    try:
        selected_choice = Flight.objects.filter(airplane_from__eq=request.GET['from'])
    except (KeyError):
        return render(request, "tripplanner/planner.html",
            {"error_message": "Please select the city you are planning to travel to."})

def plan_trip(request):
    print(request.POST)

    # Cities
    city_from = City.objects.filter(name=request.POST['city_from'][0])[0]
    city_to = City.objects.filter(name=request.POST['city_to'][0])[0]



    # Times
    try:
        start_date = dt.datetime.strptime(request.POST['start_date'][0], "%d/%m/%Y", 
            tzinfo=pytz.timezone("Australia/Sydney"))
        end_date = dt.datetime.strptime(request.POST['end_date'][0], "%d/%m/%Y", 
            tzinfo=pytz.timezone("Australia/Sydney"))
    except ValueError:
        return HttpResponseRedirect(
            reverse("triplanner:planner", args=("Invalid start and end dates",))
            )

    # Find flights
    flights = Flight.objects.filter(city_from)


    trip = Trip(city_from=city_from, city_to=city_to, 
        flight=flight, start_date=start_date, end_date=end_date)


    return HttpResponseRedirect(reverse(f'tripplanner:trip_{pk}'))

