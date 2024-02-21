from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=254)
    date = models.DateField(auto_now=True)
    blurb = models.CharField(max_length=508)
    content = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_rating(self):
        article_reviews_total = 0

        for article_review in self.article_reviews.all():
            article_reviews_total += article_review.rating

        if article_reviews_total > 0:
            return article_reviews_total / self.article_reviews.count()

        return 'No rating'

    def __str__(self):
        return self.title


class ArticleReview(models.Model):
    article = models.ForeignKey(Article, related_name='article_reviews',
                                on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='article_reviews',
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
