from django.contrib import admin
from posts.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subscribers',)


admin.site.register(Category, CategoryAdmin, )
admin.site.register(Post)
