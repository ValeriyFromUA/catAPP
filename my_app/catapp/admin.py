from django.contrib import admin
from .models import User, Posts, Images, Likes, Confirmations, PostTags

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Images)
admin.site.register(Likes)
admin.site.register(Confirmations)
admin.site.register(PostTags)
