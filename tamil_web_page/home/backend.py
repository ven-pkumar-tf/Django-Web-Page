from django.contrib.auth.backends import BaseBackend
from home.models import User  # Import the custom User model

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Use the custom User model from home
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
