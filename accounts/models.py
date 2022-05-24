from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    national_code = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)

    def __str__(self):
        return self.username
