from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
        'author': 'Anugeeth',
        'title': 'test post',
        'content': 'Test conent',
        'date_posted': '12/12/12'
    },
    {
        'author': 'tester',
        'title': 'test pdsdsdost',
        'content': 'Test dssdsdsdsDasdconent',
        'date_posted': '12/12/12'

    },
]

#  home view
def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

# about view
def about(request):
    return render(request, 'blog/about.html')
