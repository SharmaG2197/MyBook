from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class AccountManager(BaseUserManager):
  def create_user(self, email, password=None):
    """Create and return a regular user with an email and password."""
    if not email:
      raise ValueError("Users must have an email address")
    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password):
    """Create and return a superuser with an email and password."""
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

class Account(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)  # Add this field
  termsandconditions_and_privacy_policy = models.BooleanField(default=False)
  marketing_mail = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []  # You can add other required fields here

  objects = AccountManager()

    # Add unique related_name for groups and user_permissions
  groups = models.ManyToManyField('auth.Group', related_name='account_groups', blank=True)
  user_permissions = models.ManyToManyField('auth.Permission', related_name='account_user_permissions', blank=True )

  def __str__(self):
    return self.email

class AdminUser(Account):
  class Meta:
    proxy = True
    verbose_name = 'Admin User'
    verbose_name_plural = 'Admin Users'

  def save(self, *args, **kwargs):
    self.is_staff = True
    self.is_superuser = True
    super().save(*args, **kwargs)


# C:\Users\v-deepak.sharma\Desktop\BOOK\venv\my_book\accounts\models.py

