from django.test import TestCase


class TestViews(TestCase):

    def test_see_shopping_bag(self):
        """ testing view for shopping bag """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)

        template = 'bag/bag.html'
        self.assertTemplateUsed(response, template)