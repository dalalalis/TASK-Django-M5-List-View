
from rest_framework.generics import ListAPIView,RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from .models import Booking, Flight
from .serializers import FlightListSerializer, BookingListSerializer, BookingDetailSerializer, BookingCreateSerializer
from .models  import Booking
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import Is3days, IsOwner

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class= FlightListSerializer
    permission_classes=[IsAuthenticated]

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer
    permission_classes=[IsAuthenticated]

class BookingDetailedView(RetrieveAPIView):
    queryset=Booking.objects.all()
    serializer_class= BookingDetailSerializer
    lookup_field= 'id'
    lookup_url_kwarg='booking_id'
    permission_classes=[IsAuthenticated]


class BookingUpdateView(RetrieveUpdateAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingCreateSerializer
    lookup_fields='id'
    lookup_url_kwarg='object_id'
    permission_classes=[IsAuthenticated, IsAdminUser, Is3days]

class BookingDeleteView(DestroyAPIView): 
    queryset = Booking.objects.all()
    serializer_class =BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes=[IsAuthenticated, IsAdminUser, Is3days]

class BookingCreateAPIview(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class= BookingCreateSerializer
    permission_classes=[IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, flight_id=self.kwargs["object_id"])



    
