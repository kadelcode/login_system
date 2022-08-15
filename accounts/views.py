from django.shortcuts import render

# Create your views here.

#register view
def register(request):
    return render(request, 'accounts/register.html')
