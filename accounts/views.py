from django.shortcuts import render, redirect
from accounts.models import User

# def profile (request, id):
#     user = User.objects.get(pk=id)
#     context = {
#         'user':user
#     }
#     return render (request, 'profile.html', context)
 

def profile(request, slug):
    user = User.objects.get(slug=slug)
    # print(user.posts.all())
    context = {
        'user':user
    }
    return render(request, 'profile.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        user = User.objects.create(username=username, first_name=firstname, last_name=lastname, password=password)
        # user.save()
        return redirect('/')
    return render(request, 'register.html')