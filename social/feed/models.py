from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(('email address'), unique=True)
    icon = models.ImageField(upload_to='user_icons/', blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

"""class userIcons(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='user_icons/')

    def __str__(self):
        return self.profile.username"""

class userPost(models.Model):
    title = models.CharField(max_length=75)
    desc = models.TextField()
    uploaded_file = models.FileField(upload_to='posts/')
    user_profile = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    published_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title