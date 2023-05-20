from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.hashers import make_password
from django.views.generic import DetailView, CreateView
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# def profile(request, slug):
#     user = User.objects.get(slug=slug)
#     # print(user.posts.all())
#     context = {
#         'user':user
#     }
#     return render(request, 'profile.html', context)

class ProfileView(DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "user"

class RegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
 
class LoginUserView(LoginView):
    template_name = "login.html"
    form_class = LoginForm


# CreateView, DetailView, ListView, TemplateView



# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         password = request.POST.get('password')
#         user = User.objects.create(username=username, first_name=firstname, last_name=lastname, password=make_password(password))
#         # user.save() c
#         return redirect('/')
#     return render(request, 'register.html')



# def login(request):
#     if request.method == 'POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         dj_login(request, user)
#         return redirect('/')
#     return render(request, 'login.html')

  