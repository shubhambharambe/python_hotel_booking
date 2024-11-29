from django.urls import path
from .views import HotelListCreateView, RoomListView, BookingListCreateView, BookingDetailView,UserBookingListView,UserView,HotelUpdateView,RoomListCreateView,UserCreateView
from django.contrib.auth import views as auth_views
from .views import ChangePasswordView

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
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/l-sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]