from django.db import models
from django.contrib.auth.models import User


class CustomUserModel(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(null=False, blank=False, max_length= 11)
    address = models.CharField(max_length=200)
    national_code = models.CharField(max_length=10, unique=True)
    birthday = models.DateField()
    gender = models.CharField(max_length = 1,null=True, choices = GENDER_CHOICES)
    condition = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'

