from django.shortcuts import render
from .models import Article

# Create your views here.

def all_articles(request):
    """ A view to return all articles """

    articles = Article.objects.all()

    context = {
        'articles': articles 
    }

    return render(request, 'articles/articles.html', context)