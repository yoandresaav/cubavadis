from django.contrib import admin

# Register your models here.

from .models import Tours


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    pass