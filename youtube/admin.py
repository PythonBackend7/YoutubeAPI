from django.contrib import admin
from .models import Category, Hashtag, Comment, Video


# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views', 'category', 'likes',)
    list_display_links = ('id', 'title', 'views', 'category', 'likes',)
    search_fields = ('id', 'title', 'category',)
    filter_horizontal = ('hashtags',)


admin.site.register(Category)
admin.site.register(Hashtag)
admin.site.register(Comment)
