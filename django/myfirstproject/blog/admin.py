from django.contrib import admin
from .models import Category, Post,Comment
# Register your models here.

admin.site.register(Category)
#admin.site.register(Post)
admin.site.register(Comment)

#customizing the admin panel for Post model

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','author','published_date','status')
    list_filter = ('status','created_at','published_date','author')
    search_fields = ('title','content')
    raw_id_fields = ('author',)
    ordering = ['status','published_date']

admin.site.register(Post,PostAdmin)
