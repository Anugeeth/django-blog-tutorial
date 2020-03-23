from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm as forms

from django.http import HttpResponse
# Create your views here.


def register(request):

# checking whether is request is a post request or not if yes data is [passed] to the usercreation model
    if request.method == 'POST':
        form = forms(request.POST)
        if form.is_valid():
            # saving form
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            # for returning messages 
            return redirect('blog-home')

# for other requests on the same route user creation form is returned  
    else:
        form = forms()

    return render(request, 'users/register.html', {'form' : form})
    
def login(request):
    # form = UserCreationForm()
    # return render(request, 'users/register.html', {'form' : form})
    return HttpResponse('<h1>Login</h1>')