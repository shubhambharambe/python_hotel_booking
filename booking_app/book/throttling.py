from rest_framework.throttling import ScopedRateThrottle

class BookingRateThrottle(ScopedRateThrottle):
    scope = 'booking'