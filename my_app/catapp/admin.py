from django.contrib import admin
from .models import User, Posts, Tags, Images, Likes, Confirmations, PostTags

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Tags)
admin.site.register(Images)
admin.site.register(Likes)
admin.site.register(Confirmations)
admin.site.register(PostTags)
