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
            # Save the form but don't commit to the database yet
            event = form.save(commit=False)
            # Assign the currently logged-in user as the organizer
            event.organizer = request.user
            # Save the event to the database
            event.save()
            return redirect(reverse("events:event-listing"))

    else:
        form = EventForm()
    return render(request, "add_event.html", context={"form": form})


@login_required
def my_events(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, "my_events.html", context={"events": events})


@login_required
def update_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect(reverse("events:event-listing"))

    return render(request, "update_event.html", context={"form": form})
