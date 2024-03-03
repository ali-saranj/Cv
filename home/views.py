from django.shortcuts import render
from django.views.generic import CreateView

from .models import Plan, Project


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


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'phone', 'email', 'description']
    template_name = 'contact.html'
