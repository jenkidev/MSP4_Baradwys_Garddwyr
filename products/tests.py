from django.test import TestCase

from products.models import Product, Category


class TestViews(TestCase):

    def test_see_all_products(self):
        """test view to see all products"""

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

        template = 'products/products.html'
        self.assertTemplateUsed(response, template)

    def test_see_product_details(self):
        """test view to see product details"""

        category = Category.objects.create(
            name='flower',
            friendly_name='Flower'
        )

        product = Product.objects.create(
            name='Test',
            species='species',
            price=12.00,
            planting_conditions='planting_conditions',
            rating=0,
            description='description',
            category=category,

        )

        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

        template = 'products/product_detail.html'
        self.assertTemplateUsed(response, template)
