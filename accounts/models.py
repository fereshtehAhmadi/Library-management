from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserModel(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(null=False, blank=False, unique=True, max_length= 11) # PhoneNumberField, CharField
    address = models.CharField(max_length=200)
    national_code = models.CharField(max_length=10)
    birthday = models.DateField()
    gender = models.CharField(max_length = 1,null=True, choices = GENDER_CHOICES)
    debt = models.OneToOneField("loan.DebtModel",null=True, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.user.username}'

