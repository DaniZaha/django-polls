from django.test import TestCase
from django.utils import timezone, dateformat
from .models import Article, User, Comment

# class CategoryModelTest(TestCase): 
# 	@classmethod
# 	def setUpTestData(cls):
# 		Category.objects.create(category='Innovations', slug='innovations')

# 	def test_get_absolute_url(self): 
# 		category=Category.objects.get(id=1)
# 		self.assertEquals(category.get_absolute_url(), '/articles/category/innovations')

class TestTest(TestCase):
	def test_test_file(self):
		print('test file 2 is working')

class ArticleModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		print('setup')
		u = User.objects.create(username = 'nobody', password='123')
		Article.objects.create(article_author = u,  article_title = 'test', article_text = 'Hello test', ppub_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s'))
		
	def test_get(self):
		a = Article.objects.get(id = 1)
		print('testing article')
		print(a)
		self.assertEquals(a.was_recent(), True)
		self.assertEquals(a.num_likes, 0)
