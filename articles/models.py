from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=254)
    blurb = models.CharField(max_length=508)
    content = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

