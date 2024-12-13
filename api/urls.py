from django.urls import path
from .views import *

urlpatterns = [
    path("events/", event_list, name="event-list-api"),
    path("events/<int:pk>/", EventDetail.as_view(), name="event-detail-api"),
]
