from django.contrib import admin

from home.models import Plan, Project, Post, Author

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
