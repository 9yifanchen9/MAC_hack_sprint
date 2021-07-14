from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name = "tripplanner/index.html"

