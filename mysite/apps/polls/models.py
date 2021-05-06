from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone, dateformat

class Article(models.Model):
	article_author = models.ForeignKey(User, default=0, blank=True, null=False, on_delete=models.CASCADE, related_name='article_author_user')
	article_title = models.CharField('article name', max_length = 200)
	article_text = models.TextField('article text')
	ppub_date = models.DateTimeField('pub date')
	liked = models.ManyToManyField(User, default=None, blank=True)

	def __str__(self):
		return self.article_title

	def was_recent(self):
		return self.ppub_date >= (timezone.now() - datetime.timedelta(days = 7))

	@property
	def num_likes(self):
		return self.liked.all().count()


LIKE_CHOISE = ( ('Like', 'Like'), ('Unlike', 'Unlike') )

class Like(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	val = models.CharField(choices=LIKE_CHOISE, default='like', max_length=10)
	
	def __str__(self):
		return str(self.article)

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('author name', max_length = 50)
	comment_text = models.CharField('comment text', max_length = 200)

	def __str__(self):
		return self.author_name

	def get_time_com():
		return dateformat.format(timezone.now(), 'Y-m-d H:i:s')