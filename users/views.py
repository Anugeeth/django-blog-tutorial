from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm as UserRegForm

# Create your views here.


def register(request):
# checking whether is request is a post request or not if yes data is [passed] to the usercreation model
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            # saving form
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, Login now!!!')

            # for returning messages 
            return redirect('login')

# for other requests on the same route user creation form is returned  
    else:
        form = UserRegForm()

    return render(request, 'users/register.html', {'form' : form})

@login_required    
def profile(request):

    return render(request, 'users/profile.html')