from rest_framework import serializers
from .models import Hotel, Room, Booking
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())  # Accept hotel ID

    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    hotel_name = serializers.CharField(source='room.hotel.name', read_only=True)  # Add hotel name

    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields, including hotel_name

    def validate(self, data):
        """
        Add validations for:
        1. Room availability
        2. Start date being earlier than or equal to the end date
        """
        room = data['room']
        start_date = data['start_date']
        end_date = data['end_date']

        # Validate room availability
        if not room.is_available:
            raise serializers.ValidationError(f"The room '{room}' is not available for booking.")

        # Validate start and end dates
        if start_date > end_date:
            raise serializers.ValidationError("The start date cannot be later than the end date.")

        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
