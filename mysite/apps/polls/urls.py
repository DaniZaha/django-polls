from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('keys/', views.keys, name = 'keys'),
	path('create_article/', views.create_article, name = 'create_article'),
	path('register/', views.register, name = 'register'),
	path('logingin/', views.logingin, name = 'logingin'),
	path('logingout/', views.logingout, name = 'logingout'),
	path('<int:article_id>/', views.detail, name = 'detail'),
	path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
	path('<int:article_id>/leave_like/', views.leave_like, name = 'leave_like'),
	path('<int:article_id>/leave_dislike/', views.leave_dislike, name = 'leave_dislike'),
]