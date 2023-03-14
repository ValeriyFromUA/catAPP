from django.contrib import admin
from .models import User, Posts, Tags, Images, Likes, Confirmations, PostTags


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_confirmed', 'created_at')
    list_filter = ('is_confirmed',)
    search_fields = ('email', 'username')
    ordering = ('-created_at',)


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_id', 'created_at')
    list_filter = ('tags',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image_path', 'preview_image_path', 'post_id')


class LikesAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'post_id', 'is_liked', 'created_at')


class ConfirmationsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'confirmation_key', 'created_at')


class PostTagsAdmin(admin.ModelAdmin):
    list_display = ('post', 'tag')


admin.site.register(User, UserAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(Confirmations, ConfirmationsAdmin)
admin.site.register(PostTags, PostTagsAdmin)
