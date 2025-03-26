from django.contrib import admin
from .models import User, UserProfile, Event, Feedback

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Feedback)
