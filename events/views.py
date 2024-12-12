from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

# Create your views here.


@login_required
def event_listing(request):
    event = Event.objects.all()
    return render(request, "event_listing.html", {"events": event})


@login_required
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, "event_detail.html", {"event": event})


@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            event.organizer = request.user
            event.save()
            return redirect(reverse("events:event-listing"))

    else:
        form = EventForm()
    return render(request, "add_event.html", context={"form": form})
