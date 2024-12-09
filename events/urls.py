from django.urls import path
from .views import event_listing, event_detail

urlpatterns = [
    path("", event_listing, name="event-listing"),
    path("<int:event_id>/", event_detail, name="event-detail"),
]
