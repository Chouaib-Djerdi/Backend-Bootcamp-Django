from django.urls import path
from .views import *

app_name = "events"

urlpatterns = [
    path("", event_listing, name="event-listing"),
    path("<int:event_id>/", event_detail, name="event-detail"),
    path("add-event/", add_event, name="add-event"),
    path("update-event/<int:pk>/", update_event, name="update-event"),
    path("my-events/", my_events, name="my-events"),
    path("delete-event/<int:pk>/", delete_event, name="delete-event")
]
