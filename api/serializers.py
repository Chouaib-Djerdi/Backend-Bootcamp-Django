from rest_framework import serializers
from events.models import Event
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]


class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)  # Nested serializer for organizer
    attendees = UserSerializer(
        many=True, read_only=True
    )  # Nested serializer for attendees

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "date",
            "location",
            "max_seats",
            "organizer",
            "attendees",
        ]
