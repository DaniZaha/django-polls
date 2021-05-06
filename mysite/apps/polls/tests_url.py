from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve

from .views import index, register, logingin, logingout, create_article, detail, keys, leave_comment, leave_like, leave_dislike

class TestTest(TestCase):
	def test_test_file(self):
		print('test file is working')

class HomeTests(TestCase):
	def test_home_view_status_code(self): 
		url = reverse('articles:index')
		response = self.client.get(url) 
		self.assertEquals(response.status_code, 200)

	def test_home_url_resolves_home_view(self):
		view = resolve('/polls/')
		print(view.func)
		self.assertEquals(view.func, index)


class RegisterTests(TestCase):
	def test_reg_view_status_code(self): 
		url = reverse('articles:register')
		response = self.client.get(url) 
		self.assertEquals(response.status_code, 200)

	def test_reg_url_resolves_reg_view(self):
		view = resolve('/polls/register/')
		print(view.func)
		self.assertEquals(view.func, register)


class LoginTests(TestCase):
	def test_login_url_resolves_login_view(self):
		view = resolve('/polls/logingin/')
		print(view.func)
		self.assertEquals(view.func, logingin)


class LogoutTests(TestCase):
	def test_logout_url_resolves_logout_view(self):
		view = resolve('/polls/logingout/')
		print(view.func)
		self.assertEquals(view.func, logingout)


class CreateArticleTests(TestCase):
	def test_create_article_view_status_code(self): 
		url = reverse('articles:create_article')
		response = self.client.get(url) 
		self.assertEquals(response.status_code, 200)

	def test_create_article_url_resolves_create_article_view(self):
		view = resolve('/polls/create_article/')
		print(view.func)
		self.assertEquals(view.func, create_article)


class DetailTests(TestCase):
	# def test_detail_view_status_code(self): 
	# 	url = reverse('articles:detail',  args=(1,))
	# 	print(url)
	# 	response = self.client.get(url) 
	# 	self.assertEquals(response.status_code, 200)

	def test_detail_url_resolves_detail_view(self):
		view = resolve('/polls/1/')
		print(view.func)
		self.assertEquals(view.func, detail)


class KeysTests(TestCase):
	def test_reg_view_status_code(self): 
		url = reverse('articles:keys')
		response = self.client.post(url, {'key_words' : 'test'}) 
		self.assertEquals(response.status_code, 200)

	def test_reg_url_resolves_reg_view(self):
		view = resolve('/polls/keys/')
		print(view.func)
		self.assertEquals(view.func, keys)


# class CommentTests(TestCase):
	# def test_leave_comment_view_status_code(self): 
	# 	url = reverse('articles:leave_comment',  args=(1,))
	# 	print(url)
	# 	response = self.client.post(url, {'text' : 'test'}) 
	# 	self.assertEquals(response.status_code, 200)

	# def test_leave_comment_url_resolves_leave_comment_view(self):
	# 	view = resolve('/polls/1/leave_comment')
	# 	print(view.func)
	# 	self.assertEquals(view.func, detail)

	