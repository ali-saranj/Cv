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


def blog(request):
    weblog = Post.objects.all()
    context = {"blog": weblog}
    return render(request, 'weblogPage.html', context)


def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'weblog_details.html', {'post': post})


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'phone', 'email', 'description']
    template_name = 'contact.html'


# get_blog
class BlogView(TemplateView):
    template_name = 'weblogPage.html'

    def get_context_data(self):
        context = super().get_context_data()
        posts = Post.objects.all()
        context['posts'] = posts
        return context

# class Create_weblog(CreateView):
#     model = Post
#     fields = ['image', 'title', 'content', 'author']
#     template_name = 'contact.html'
