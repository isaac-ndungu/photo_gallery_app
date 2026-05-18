from django.contrib import admin
from .models import Tag, Photo

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    list_filter = ('created_at', 'tags')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)
