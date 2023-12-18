from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, default='', on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    species = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    planting_conditions = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    clearance = (models.BooleanField(default=False, null=True, blank=True))
    new_arrival = (models.BooleanField(default=False, null=True, blank=True))
    deals = (models.BooleanField(default=False, null=True, blank=True))
    image = models.ImageField(null=True, blank=True)

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating
        
        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        
        return 'No rating'

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)