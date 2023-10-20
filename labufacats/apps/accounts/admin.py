from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo_post', 'data_post']
    list_filter = ['data_post']
    # search_fields = ['autor']
    

admin.site.site_header = 'La Bufa Cats'
admin.site.site_title = 'La Bufa Cats'