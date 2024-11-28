from django.urls import path
from .views import HotelListCreateView, RoomListView, BookingListCreateView, BookingDetailView,UserBookingListView,UserView,HotelUpdateView,RoomListCreateView,UserCreateView

urlpatterns = [
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotel/upd/<int:pk>', HotelUpdateView.as_view(), name='hotel-update-retrive'),
    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('mybookings/', UserBookingListView.as_view(), name='user-bookings'),
    path('users/list/', UserView.as_view(), name='user-create'),
    path('users/create/', UserCreateView.as_view(), name='user-list'),
    path('room/create/', RoomListCreateView.as_view(), name='room-create'),
]