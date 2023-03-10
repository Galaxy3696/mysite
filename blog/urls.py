from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^(?P<slug>[\w]+)/$', views.category, name='category'),
    path('blog/<int:article_id>/', views.article, name="blog"),
    path('comment/<int:article_id>/<int:comment_id>/', views.article, name="comment"),
    path('dates/<int:year>/<int:month>/', views.blog_get_dates, name="dates"),   # 归档页
]