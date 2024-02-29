#def detectUser(user):
#    if user.is_superadmin:
#        redirectUrl = '/admin'
#    elif user.role == 1:
#        redirectUrl = 'vendorDashboard'
#    elif user.role == 2:
#        redirectUrl = 'custDashboard'
#    else: # Handle other cases or set a default URL
#        return redirect(redirectUrl)

from django.shortcuts import redirect


def detectUser(user):
    if user.role == 1:
        redirectUrl = 'vendorDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'

        return redirect (redirectUrl)