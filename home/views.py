from tokenize import Comment

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .models import Plan, Project, Post, Contact, Coment_Posts, Contact_us


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class plans(TemplateView):
    template_name = 'plans.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        p = Plan.objects.all()
        context['p'] = p
        return context


def content(request):
    return render(request, 'contact.html')


def blog(request):
    weblog = Post.objects.all()
    new_posts = Post.objects.filter(is_featured=True)
    context = {"blog": weblog, "new_posts": new_posts}
    return render(request, 'weblogPage.html', context)


class is_featured(TemplateView):
    template_name = 'weblogPage.html'

    def get_context_data(self):
        context = super().get_context_data()
        is_featured = Post.objects.filter(is_featured=True)
        context['is_featured'] = is_featured
        return context


def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'weblog_details.html', {'post': post})


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'phone', 'email', 'description']
    template_name = 'contact.html'


# content
def content_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        content = Contact(name=name, email=email, phone=phone, description=description)
        content.save()
        contxt = {
            'response': "اطلاعات ذخیره شد با شما تماس خواهیم گرفت"
        }

        return render(request, 'contact.html', {'content': contxt})
    else:
        return HttpResponse("Method not allowed", status=405)


def comment_post(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')  # Changed 'content' to 'comment'
        comment = Coment_Posts(name=name, email=email, content=comment)
        comment.save()
        context = {
            'response': "اطلاعات ذخیره شد"
        }

        return render(request, 'weblog_details.html', {'context': context})  # Changed 'contaxt' to 'context'
    else:
        return HttpResponse("Method not allowed", status=405)


# get_post_comment
def get_comment(request):
    comments = Coment_Posts.objects.all()
    return render(request, 'weblog_details.html', {'comments': comments})


# ارتباط با ما در صفحه پلن
def Contact_us_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        add_form = Contact_us(name=name, email=email, phone=phone, location=location)
        add_form.save()
        context = {
            'response': "اطلاعات ذخیره شد"
        }
    return render(request, 'contact_us.html')


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
