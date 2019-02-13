from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Allows Django work with custom user model"""

    def create_user(self, email, name, password=None):
        """Create new user"""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create new superuser"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile"""


    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Set object manager to substitute custom model
    objects = UserProfileManager()

    # Overwrite username to use email address to login
    USERNAME_FIELD = 'email'

    # only name as email is already required
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get users full name"""

        return self.name

    def get_short_name(self):
        """Get user short name"""

        return self.name

    # print user profile

    def __str__(self):

        return self.email



class ProfileFeedItem(models.Model):
    """Profile status update"""

    # Get user profile
    user_profile = models.ForeignKey('USerProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.status_text












