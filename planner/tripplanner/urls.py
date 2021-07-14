from django.urls import path

from . import views

app_name = "tripplanner"
urlpatterns = [
    path('', views.home_view, name='home'),
    path('planner/', views.planner_view, name="planner")
]