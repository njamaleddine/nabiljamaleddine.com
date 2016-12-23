from django.contrib import admin

from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'published', 'created', 'modified')
    list_filter = ('created', 'modified', 'published')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('name',)
