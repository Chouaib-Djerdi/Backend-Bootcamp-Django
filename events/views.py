from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def event_listing(request):
    event = Event.objects.all()
    return render(request, "event_listing.html", {"events": event})


@login_required
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, "event_detail.html", {"event": event})
