"""
This module defines custom throttling classes for the Job Search API.

The API uses Django Rest Framework's built-in throttling classes as a base.
It includes separate throttling classes for anonymous and authenticated users,
and for sustained and burst traffic.

Throttling is used to control the rate of requests that clients can make to the API.
"""
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonSustainedThrottle(AnonRateThrottle):
    """
    Throttle class for anonymous users for sustained traffic.

    The rate of requests is defined in the Django settings with the scope 'anon_sustained'.
    """
    scope = "anon_sustained"


class AnonBurstThrottle(AnonRateThrottle):
    """
    Throttle class for anonymous users for burst traffic.

    The rate of requests is defined in the Django settings with the scope 'anon_burst'.
    """
    scope = "anon_burst"


class UserSustainedThrottle(UserRateThrottle):
    """
    Throttle class for authenticated users for sustained traffic.

    The rate of requests is defined in the Django settings with the scope 'user_sustained'.
    """
    scope = "user_sustained"


class UserBurstThrottle(UserRateThrottle):
    """
    Throttle class for authenticated users for burst traffic.

    The rate of requests is defined in the Django settings with the scope 'user_burst'.
    """
    scope = "user_burst"
