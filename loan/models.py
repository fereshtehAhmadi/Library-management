from django.db import models
from accounts.models import CustomUserModel
from books.models import Book

from datetime import datetime


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
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.user.username} has {self.book} and loan is in {self.status} faze'
    
    
    def get_end_date():
        pass
    
    
    def diff_time(self):
        date_format = "%m/%d/%Y"
        if status == 'S':
            end = datetime.strptime(str(datetime.now().date()), date_format)
            start = datetime.strptime(str(self.start_date), date_format)
            diff = b - a
        return diff.days


class DebtModel(models.Model):
    amount = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}'