from django.db import models
from accounts.models import CustomUserModel


class LoanModel(models.Model):
    LOAN_STATUS = (
        ('C', 'choosing'),
        ('S', 'started'),
        ('R', 'returned'),
        ('T', 'to_be_returned'),
    )
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS)

    def __str__(self):
        return f'{self.user.user.username} has {self.books} and loan is in {self.status} faze'


class DebtModel(models.Model):
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.amount}'