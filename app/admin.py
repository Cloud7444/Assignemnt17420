from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):

    list_display = ['author','post_date']
    search_fields = ['author']




admin.site.register(Post,PostAdmin)
admin.site.register(AuthorList)
admin.site.register(UserProfile)
admin.site.register(like)