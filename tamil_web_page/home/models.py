from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models

# Custom User Manager to handle user creation and superuser creation
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a normal user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


# Custom User Model extending AbstractBaseUser
class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed password, not plain text
    user_role = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Admin')])

    # Default fields provided by AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Required fields for user creation
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'user_role']

    # Use the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'  # Table name in the database

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=255)
    event_description = models.TextField()
    event_organizer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name

    class Meta:
        db_table = 'events'
        managed = True  # Let Django manage the table schema

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)