from django.contrib import admin

from home.models import Plan, Project, Post, Author, Contact, Coment_Posts, Grouping, Contact_us

# Register your models here.


admin.site.register(Author)


@admin.register(Plan)
class Admin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phone', 'email', 'description']


admin.site.register(Grouping)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description']


@admin.register(Coment_Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'content']


@admin.register(Contact_us)
class Contact_us_Admin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'location']
