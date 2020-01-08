from django.contrib import admin
from blog.models import Post, Tag, Comment, Subscriber

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'active')
    list_filter = ('email', 'active')
    search_fields = ('email', 'active')

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscriber, SubscriberAdmin)