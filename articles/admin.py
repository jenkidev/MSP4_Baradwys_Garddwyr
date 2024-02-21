from django.contrib import admin
from .models import Article, ArticleReview

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


class ArticleReviewAdmin(admin.ModelAdmin):
    list_display = (
        'article',
        'rating',
        'content',
        'created_by',
        'created_at',
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleReview, ArticleReviewAdmin)
