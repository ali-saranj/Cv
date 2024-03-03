from django.contrib import admin

from home.models import Plan


# Register your models here.

@admin.register(Plan)
class Admin(admin.ModelAdmin):
    list_display = ['pk', 'name']
