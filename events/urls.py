from django.urls import path
from .views import event_listing, event_detail, add_event

app_name = "events"

urlpatterns = [
    path("", event_listing, name="event-listing"),
    path("<int:event_id>/", event_detail, name="event-detail"),
    path("add-event/", add_event, name="add-event"),
]
