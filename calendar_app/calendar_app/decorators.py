from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    #create descorator and pass in view
    def decorator(view_func):
        #Wrapper
        def wrapper_func(request, *args, **kwargs):
            #debug & print allowed
            print('role', allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            print(group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator