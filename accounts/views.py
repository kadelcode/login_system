from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

#dashboard
def dashboard(request):
    return render(request,'accounts/dashboard.html')

#register view
def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password != password1:
            messages.info(request,'Password does not match')
            return redirect('register')
        else:
            #create a user in the database
            user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)
            messages.info(request,'Account successfully created')
            return redirect('dashboard')
    else:
        return render(request, 'accounts/register.html')
