from django.contrib import admin

from .models import Confirmations, Images, Likes, Posts, PostTags, User

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Images)
admin.site.register(Likes)
admin.site.register(Confirmations)
admin.site.register(PostTags)
