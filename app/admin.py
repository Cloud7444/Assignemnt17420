from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):

    list_display = ['author','post_date']
    search_fields = ['author']
    list_filter = ['post_date']

class UserprofileAdmin(admin.ModelAdmin):
    fields = ['phone','address','pic']




admin.site.register(Post,PostAdmin)
admin.site.register(AuthorList)
admin.site.register(UserProfile,UserprofileAdmin)
admin.site.register(like)