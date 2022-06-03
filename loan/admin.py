from django.contrib import admin
from loan.models import LoanModel, DebtModel


admin.site.register(LoanModel)
admin.site.register(DebtModel)
