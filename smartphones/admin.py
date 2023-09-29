from django.contrib import admin
from .models import Smartphone, Category


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description", "time_create", "time_update"]
    fields = ("name", "description", "category")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description"]
    fields = ("title", "description")
