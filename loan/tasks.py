from loan.models import LoanModel, DebtModel
from django.contrib.auth.models import User
from accounts.models import CustomUserModel


  
def expiration():
    loan = LoanModel.objects.all()
    for obj in loan:
        if datetime.now() >= obj.expiration:
            obj.status = 'T'
            obj.save()
    return None


def diff_time():
    loan = LoanModel.objects.filter(status='T')
    for obj in loan:
        diff = datetime.now() - loan.expiration
        a = int(diff.days) / 7           
        return debt(a=a, book=loan.book)
    
    
def debt(a, book):
    debt = DebtModel.objects.get(book=book)
    debt.amount = a * 2000
    debt.save()
    return debt.amount



    



# def expiration():
#     custom_user = CustomUserModel.objects.get(user=request.user)
#     loan = LoanModel.objects.filter(user=custom_user)
#     for obj in loan:
#         if datetime.now() >= obj.expiration:
#             obj.status = 'T'
#             obj.save()
#             return obj.status
    
# def diff_time():
#     custom_user = CustomUserModel.objects.get(user=request.user)
#     loan = LoanModel.objects.filter(user=custom_user, status='T')
#     for obj in loan:
#         diff = datetime.now() - loan.expiration
#         a = int(diff.days) / 7           
#         return debt(a=a, book=loan.book)
    
    
# def debt(a, book):
#     debt = DebtModel.objects.get(book=book)
#     debt.amount = a * 2000
#     debt.save()
#     return debt.amount


# def sum_debt(sum=0):
#     debt = DebtModel.objects.filter(user=request.user)
#     for obj in debt:
#         sum += int(obj.amount)
#         return sum_debt(sum)
#     return sum