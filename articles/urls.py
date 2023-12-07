from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('<article_id>', views.article_details, name='article_details'),
]
