from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):

    # list_display = ['author','post_date']
        search_fields = ['author']
admin.site.register(Post,PostAdmin)