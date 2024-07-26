from django.contrib import admin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'surname',)
    list_display_links = ('id', 'email', 'name', 'surname',)
    search_fields = ('id', 'email', 'name',)
