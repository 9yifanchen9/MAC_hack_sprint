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

def index(request):
    return HttpResponse("hello world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name = "tripplanner/index.html"

