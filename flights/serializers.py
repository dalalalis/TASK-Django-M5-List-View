from rest_framework import serializers
from flights.models import Booking, Flight 

class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Flight
        fields=['id','destination','time','price']

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'id',]

class BookingDetailSerializer(serializers.ModelSerializer):
    model= Booking
    fields=['id','flight','date','passengers']

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields=['passengers','date']