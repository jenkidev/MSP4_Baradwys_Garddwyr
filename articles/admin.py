from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'date',
        'blurb',
        'content',
        'rating',
        'image',
    )

    ordering = ('pk',)


admin.site.register(Article, ArticleAdmin)