from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hotel, Room, Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'location','description','Amenities','hotel_rules','delux_rooms_count','semidelux_room_count','created_at')  # Display these fields in the admin list view
    search_fields = ('name', 'location')  # Enable search by these fields
    list_filter = ('created_at',)  # Enable filtering by creation date

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_type', 'price_per_night', 'is_available')  # Display fields
    list_filter = ('hotel', 'room_type', 'is_available')  # Enable filtering
    search_fields = ('hotel__name', 'room_type')  # Search by hotel name and room type

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_date', 'end_date', 'total_price')  # Display fields
    list_filter = ('start_date', 'end_date', 'room__hotel')  # Filter by dates and hotel
    search_fields = ('user__username', 'room__hotel__name')  # Search by user and hotel name
    date_hierarchy = 'start_date'  # Add a date-based drill-down navigation
