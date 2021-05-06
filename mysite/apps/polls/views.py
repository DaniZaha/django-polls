from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
import datetime
from django.utils import timezone, dateformat
from .models import Article, Comment, Like, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

def index(request):
	latest_articles = Article.objects.order_by('-ppub_date')
	return render(request, 'articles/list.html', {'latest_articles': latest_articles});

def register(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect( reverse('articles:index') )

	cont = {'form' : form}
	return render(request, 'articles/register.html', cont)

def logingin(request):
	username = request.POST['username']
	password = request.POST['psswrd']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect( request.META.get('HTTP_REFERER') )
        	# return HttpResponseRedirect( reverse('articles:index'))
		else:
			messages.info(request, "This user is blocked")
			return HttpResponseRedirect( request.META.get('HTTP_REFERER')) 

	else:
		messages.info(request, "Wrong user/password data")
		return HttpResponseRedirect( request.META.get('HTTP_REFERER') )


def logingout(request):
    logout(request)
    return HttpResponseRedirect( reverse('articles:index'))


def create_article(request):

	if request.method == 'POST' and len(request.POST['article_title']) in range(1, 200):
		if 'anon_article' not in request.POST:
			a = Article(article_text = request.POST['article_text'], article_title = request.POST['article_title'], article_author = request.user, ppub_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s'))
			a.save()
		else:
			a = Article(article_text = request.POST['article_text'], article_title = request.POST['article_title'], article_author = User.objects.get(id = 0), ppub_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s'))
			a.save()
		return redirect( reverse('articles:index') )

	return render(request, 'articles/create_article.html')


def detail(request, article_id):
	try:
	 	a = Article.objects.get(id = article_id)
	 	user = request.user
	except:
		raise Http404("Хммм похоже такого тут нету...")

	latest_comments_list = a.comment_set.order_by('-id')

	return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list, 'user' : user})

def keys(request):
	key_words = request.POST['key_words'].split()
	q = ' OR '.join(["article_text LIKE %s" for i in key_words])
	n = ['%%' + i + '%%' for i in key_words]
	matching_articles = Article.objects.raw("SELECT * FROM polls_article WHERE " + q, n)
	print(matching_articles)
	return render(request, 'articles/keys.html', {'matching_articles': matching_articles});

def leave_comment(request, article_id):
	try:
	 	a = Article.objects.get(id = article_id)
	except:
	 	raise Http404("Хммм похоже такого тут нету...")

	if request.user.is_authenticated:
		username = request.user.username

	txt = request.POST['text'].replace('!time', str(Comment.get_time_com()) ) 
	
	a.comment_set.create(author_name = username, comment_text = txt)

	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )

def leave_like(request, article_id):
	try:
	 	a = Article.objects.get(id = article_id)
	 	user = request.user
	except:
	 	raise Http404("Хммм похоже такого тут нету...")

	if request.method == 'POST':
		if user in a.liked.all():
			a.liked.remove(user)
		else:
			a.liked.add(user)

		like, created = Like.objects.get_or_create(user=user, article=a)

		if not created:
			if like.val == 'Like':
				like.val = 'Unlike'
			else:
				like.val = 'Like'


		like.save()

	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )

def leave_dislike(request, article_id):
	try:
	 	a = Article.objects.get(id = article_id)
	except:
	 	raise Http404("Хммм похоже такого тут нету...")

	if 'dislike' not in request.GET:
		raise Http404("Хммм жопа")
	else: 
		a.dislikes = a.dislikes + 1
		a.save() 

	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )
