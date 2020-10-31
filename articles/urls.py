from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/edit/', views.ArticleUpdate.as_view(), name='article_edit'),
    path('<int:pk>/delete/', views.ArticleDelete.as_view(), name='article_delete'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new')
]