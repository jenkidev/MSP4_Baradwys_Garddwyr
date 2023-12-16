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
    """ Add an article to the site """
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added article!')
            return redirect(reverse('add_article'))
        else:
            messages.error(request, 'Failed to add article. Please ensure the form is valid.')
    else:
        form = ArticleForm()
        
    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_article(request, article_id):
    """ Edit a article in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('article_details', args=[article.id]))
        else:
            messages.error(request, 'Failed to update article. Please ensure the form is valid.')
    else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are editing {article.title}')

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article,
    }

    return render(request, template, context)