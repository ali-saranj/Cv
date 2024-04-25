from django.contrib import admin

from home.models import Plan, Project, Post, Author, Contact, Coment_Posts

# Register your models here.


admin.site.register(Author)


@admin.register(Plan)
class Admin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phone', 'email', 'description']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author']


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description']


@admin.register(Coment_Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'content']
