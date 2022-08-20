from email import message
from urllib import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import NameForm

# Create your views here.


#My PerSonaL View
def addiview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = NameForm(request.POST)
        # check whether the form is valid
        if form.is_valid():
            messages.info(request, 'You have successfully submitted the form.')
            return redirect('addiview')
        else:
            messages.error(request, 'Form not submitted!')
            return redirect('addiview')
    else:
        form = NameForm()
    return render(request,'accounts/additionalinfo.html',{'form':form})


#login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticating the user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'You are not currently authenticated. Please register to get started!')
            return redirect('register')

    else:
        return render(request, 'accounts/login.html')


#dashboard
@login_required
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
            auth_user = authenticate(username = username, password = password)
            login(request, auth_user)
            return redirect('dashboard')
    else:
        return render(request, 'accounts/register.html')

#logout view
def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')
