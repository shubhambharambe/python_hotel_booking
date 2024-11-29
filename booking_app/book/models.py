from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    Amenities = models.CharField(max_length=255, default='NA')
    hotel_rules = models.CharField(max_length=255, default='NA')
    created_at = models.DateTimeField(auto_now_add=True)
    delux_rooms_count = models.PositiveIntegerField(default=0)
    semidelux_room_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
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

        # Send email notification
        self.send_booking_email()

    def send_booking_email(self):
        subject = f"Booking Confirmation - {self.room.hotel.name}"
        booking_details = {
            'user_name': self.user.username,
            'hotel_name': self.room.hotel.name,
            'room_type': self.room.room_type,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'total_price': self.total_price,
        }
        html_message = render_to_string('emails/booking_confirmation.html', {'booking_details': booking_details})
        plain_message = strip_tags(html_message)
        from_email = 'your_email@gmail.com'
        to_email = [self.user.email]

        send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
        
    # Existing fields...

    def save(self, *args, **kwargs):
        # Check if it's a new booking
        is_new_booking = self._state.adding
        if is_new_booking and self.room.is_available:
            self.room.is_available = False  # Mark room as unavailable
            self.room.hotel.semidelux_room_count -= 1
            self.room.hotel.save()
            self.room.save()

        # Call the parent save
        super().save(*args, **kwargs)

        # Send booking email
        self.send_booking_email()

    def delete(self, *args, **kwargs):
        # Make room available again
        self.room.is_available = True
        self.room.hotel.semidelux_room_count += 1
        self.room.hotel.save()
        self.room.save()

        super().delete(*args, **kwargs)

