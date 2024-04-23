"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name="home"),
                  path('about', views.about, name="about"),
                  path('plans', views.plans, name="plans"),
                  path('contact', views.ProjectCreateView.as_view(), name="contact"),
                  path('content_data', views.content_data, name="content_data"),
                  path('blog', views.blog, name="blog"),
                  path('blog_details/<int:pk>', views.blog_details, name='blog_details')
                  # path('create_weblog', views.Create_weblog.as_view(), name="create_weblog"),
                  # path('blog', views.BlogView.as_view(), name='blog'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
