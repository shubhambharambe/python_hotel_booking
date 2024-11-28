from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    Amenities=models.CharField(max_length=255,default='NA')
    hotel_rules=models.CharField(max_length=255,default='NA')
    created_at = models.DateTimeField(auto_now_add=True)
    available_rooms_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)#hotel_id 
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} in {self.hotel.name}"

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate total price
        nights = (self.end_date - self.start_date).days
        self.total_price = nights * self.room.price_per_night
        super().save(*args, **kwargs)