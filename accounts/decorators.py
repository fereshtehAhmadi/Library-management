from django.shortcuts import redirect
from django.http import HttpResponse


# Check if user is logged in or not
# Authenticated users can not go to login, register again
def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper


def super_user(view_func):
    def wrapper(request, *args, **kwargs):

        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are Not authorized to view this page!!')

    return wrapper



def staff_user(view_func):
    def wrapper(request, *args, **kwargs):

        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are Not authorized to view this page!!')

    return wrapper



# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper(request, *args, **kwargs):
            
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name

#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('You are Not authorized to view this page.')

#         return wrapper
#     return decorator