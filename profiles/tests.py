from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_profile(self):
        """ test profile view """

        self.user = User.objects.create_user(
            username='MFDOOM',
            password='ALLCAPS'
        )

        self.client.login(username='MFDOOM', password='ALLCAPS')

        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 200)

        template = 'profiles/profile.html'
        self.assertTemplateUsed(response, template)
