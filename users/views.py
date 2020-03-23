from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.http import HttpResponse
# Create your views here.


def register(request):

# checking whether is request is a post request or not if yes data is posted to the user model
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            # for returning messages 
            return redirect('blog-home')
# for other requests on the same route user creation form is returned  
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form' : form})
    
def login(request):
    # form = UserCreationForm()
    # return render(request, 'users/register.html', {'form' : form})
    return HttpResponse('<h1>Login</h1>')