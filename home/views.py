from django.shortcuts import render
from .models import Plan


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def plans(request):
    p = Plan.objects.all()
    content = {"plans": p}
    return render(request, 'plans.html', content)


