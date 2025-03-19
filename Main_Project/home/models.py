# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        db_table = 'contact_us_feedback'  # Ensure data goes into the correct table

    def __str__(self):
        return f"{self.name} - {self.email}"

class EventDetails(models.Model):
    event_title = models.CharField(max_length=255)
    description = models.TextField()
    organiser_name = models.CharField(max_length=255)
    event_datetime = models.DateTimeField()
    overall_seats = models.IntegerField()
    registered_seats = models.IntegerField()
    event_link = models.URLField(blank=True, null=True)  # Optional event link

    class Meta:
        db_table = 'event_details'  # Ensure it maps to the correct Azure SQL table

    def __str__(self):
        return self.event_title

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=50)
    class Meta:
        db_table = 'login_users'
    def __str__(self):
        return self.username