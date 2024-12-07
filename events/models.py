from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    max_seats = models.IntegerField()
    # organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    # attendees = models.ManyToManyField(
    #     User, related_name="attending_events", blank=True
    # )

    def __str__(self):
        return self.title
