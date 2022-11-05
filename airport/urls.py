"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights.serializers import BookingListSerializer
from flights.views import BookingDetailedView, BookingUpdateView, FlightListView, BookingListView, BookingDeleteView, BookingCreateAPIview
from users.views import  UserCreateAPIview, UserLoginAPIview 


urlpatterns = [
    path("admin/", admin.site.urls),
    #works
    path("flights/", FlightListView.as_view(), name='flights-list'),
    #works
    path("bookings/", BookingListView.as_view(), name='bookings-list'),
    #works
    path("bookings/add/", BookingCreateAPIview.as_view(), name='create-booking'),
    path("detail/<int:booking_id>",BookingDetailedView.as_view(), name='booking-details'),
    path("update/<int:object_id>", BookingUpdateView.as_view(), name='update-booking'),
    path("delete/<int:object_id>", BookingDeleteView.as_view(), name='cancel-booking'),
    path("register/", UserCreateAPIview.as_view(), name='register'),
    #works
    path("login/", UserLoginAPIview.as_view(), name='login')]
    #works