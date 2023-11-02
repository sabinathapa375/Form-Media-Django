from django.shortcuts import render,redirect
from .form import RegistrationForm


# Create your views here.

def registrationForm(request):
    if (request.method == "POST"):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user_register=form.save(commit=False) # user_register variable is created where the form data are temporarly stored.
            user_register.user=request.user # The connecting the data in the user_register to the sepcific user.
            user_register.save() # Finally Saving the data 
            return redirect('')

    else:
        form = RegistrationForm()
    return render(request,'registration_form.html',{'Form':form})


def next_page(request):
    return render(request, 'next_page.html')


def home_page(request):
    return render(request, 'home.html')




    