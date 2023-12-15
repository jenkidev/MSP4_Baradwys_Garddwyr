from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.

def all_articles(request):
    """ A view to return all articles """

    articles = Article.objects.all()
    
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                articles = articles.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            articles = articles.order_by(sortkey)


    current_sorting = f'{sort}_{direction}'

    context = {
        'articles' : articles
    }

    return render(request, 'articles/articles.html', context)


def article_details(request, article_id):
    """ A view to return detail page of articles """

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article 
    }

    return render(request, 'articles/article_details.html', context)

def add_article(request):
    """ Add a product to the store """
    form = ArticleForm()
    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)