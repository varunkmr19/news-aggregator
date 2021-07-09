import datetime
from django.test import TestCase
from core.models import Article


class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(
            headline="test article",
            url="https://www.article-test.com",
            image_url="https://example_url.com",
            published_on=datetime.date,
            ideology='RW'
        )
        Article.objects.create(
            headline="test article part 2",
            url="https://www.article-test2.com",
            image_url="https://example_url2.com",
            published_on=datetime.date,
            ideology='LW'
        )

    def test_article_creation(self):
        """ Articles with correct headline """
        article_rw = Article.objects.get(ideology='RW')
        article_lw = Article.objects.get(ideology='LW')
        self.assertEqual(article_rw.headline, article_rw.__str__())
        self.assertEqual(article_lw.headline, article_lw.__str__())
