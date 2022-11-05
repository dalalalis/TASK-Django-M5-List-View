from datetime import datetime
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You must be the owner of the ticket "
    def has_object_permission(self, request, view, booking):
        return request.user.is_staff or booking.user == request.user

class Is3days(BasePermission):
    message ="Any updates should be done 3 days before."
    def has_object_permission(self, request, view, booking):
        if request.user.is_staff or booking.user == request.user:
            if request.date - datetime.now()>= 3:
                return request.user.is_staff or booking.user == request.user 
    

            
