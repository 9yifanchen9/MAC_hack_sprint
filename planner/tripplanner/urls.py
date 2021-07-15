from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'tripplanner'

urlpatterns = [
    path('', views.home_view, name = 'home'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    path('planner/', views.PlannerView.as_view(), name="planner"),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('', views.plan_trip, name='plan_trip'),
]