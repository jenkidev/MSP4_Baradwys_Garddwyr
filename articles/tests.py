from django.test import TestCase

from articles.models import Article


class TestViews(TestCase):

    def test_see_all_articles(self):
        """testing view to see all articles"""

        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

        template = 'articles/articles.html'
        self.assertTemplateUsed(response, template)

    def test_see_article_details(self):
        """testing view to see the article details"""

        article = Article.objects.create(
            title='title',
            date=(2023, 16, 12),
            blurb='blurb',
            content='content',
            rating=0

        )

        response = self.client.get(f'/articles/{article.id}/')
        self.assertEqual(response.status_code, 200)

        template = 'articles/article_details.html'
        self.assertTemplateUsed(response, template)
