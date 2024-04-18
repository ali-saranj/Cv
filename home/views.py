from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .models import Plan, Project, Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def plans(request):
    p = Plan.objects.all()
    content = {"plans": p}
    return render(request, 'plans.html', content)


def content(request):
    return render(request, 'contact.html')


def posts(request):
    return render(request, 'blog.html')


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'phone', 'email', 'description']
    template_name = 'contact.html'


# get_blog
class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, pk):
        context = super().get_context_data(pk=pk)
        posts = Post.objects.all()
        context['posts'] = posts
        return context

# class Create_weblog(CreateView):
#     model = Post
#     fields = ['image', 'title', 'content', 'author']
#     template_name = 'contact.html'
