from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.

def all_articles(request):
    """ A view to return all articles """

    articles = Article.objects.all()

    context = {
        'articles': articles 
    }

    return render(request, 'articles/articles.html', context)


def article_details(request, article_id):
    """ A view to return detail page of articles """

    article = get_object_or_404(Product, pk=product_id)

    context = {
        'article': article 
    }

    return render(request, 'articles/article_details.html', context)