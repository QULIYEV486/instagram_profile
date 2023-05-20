from django.shortcuts import render
from core.models import Post
from accounts.models import User
from django.views.generic import ListView, TemplateView

class MainView(TemplateView):
    template_name = "insta.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by('-id')
        context["users"] = User.objects.order_by('-id')
        return context


class ExploreView(ListView):
    model = Post
    template_name = 'explore.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')