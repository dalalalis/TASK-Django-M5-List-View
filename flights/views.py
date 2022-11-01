from cgitb import lookup
from rest_framework.generics import ListAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Booking, Flight
from .serializers import FlightListSerializer, BookingListSerializer, BookingDetailSerializer, BookingCreateSerializer
from .models  import Booking
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class= FlightListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer

class  BookingDetailedView(RetrieveAPIView):
    queryset=Booking.objects.all()
    serializer_class= BookingDetailSerializer
    lookup_field= 'id'
    lookup_url_kwarg='object_id'

class BookingUpdateView(UpdateAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingCreateSerializer
    lookup_fields='id'
    lookup_url_kwarg='object_id'

class BookingDeleteView(DestroyAPIView): 
    queryset = Booking.objects.all()
    serializer_class =BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class BookingListCreateList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    permission_classes = [IsAdminUser]

    #ask if correct 
    
