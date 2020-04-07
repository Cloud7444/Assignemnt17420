from django.contrib import admin

from .models import Post , AuthorList

class PostAdmin(admin.ModelAdmin):

    # list_display = ['author','post_date']
        search_fields = ['author']
admin.site.register(Post,PostAdmin)
admin.site.register(AuthorList)