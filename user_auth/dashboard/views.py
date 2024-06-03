from django.shortcuts import render,redirect
from allauth.account.decorators import verified_email_required


@verified_email_required
def profile(request):
    """ 
       show user details after successful login
       
       Arguments:
            request (HttpRequest)
        
        Returns:
            In Get: render a page  
    """
    return render(request,'dashboard/profile.html')