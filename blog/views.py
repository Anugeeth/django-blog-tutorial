from django.shortcuts import render
from django.http import HttpResponse

# importing post model
from .models import Post
# Create your views here.



#  home view
def home(request):
    context = {
        
        # fetching all posts from database
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

# about view
def about(request):
    return render(request, 'blog/about.html')
