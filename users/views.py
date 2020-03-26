from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm , ProfileUpdateForm 

# Create your views here.


def register(request):
# checking whether is request is a post request or not if yes data is [passed] to the usercreation model
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # saving form
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, Login now!!!')

            # for returning messages 
            return redirect('login')

# for other requests on the same route user creation form is returned  
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form' : form})

@login_required    
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()

            messages.success(request, f'Profile Updated')

            # for returning messages 
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'users/profile.html',context)