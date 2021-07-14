from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = "tripplanner/index.html"

