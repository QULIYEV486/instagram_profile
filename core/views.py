from django.shortcuts import render
from core.models import Post

def mainpage(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'insta.html', context)




def explore(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'explore.html', context)


def profile(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'profile.html', context)
