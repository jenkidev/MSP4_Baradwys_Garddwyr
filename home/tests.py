from django.test import TestCase


class TestViews(TestCase):

    def test_index(self):
        """ testing view for displaying the home page """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        template = 'home/index.html'

        self.assertTemplateUsed(response, template)
