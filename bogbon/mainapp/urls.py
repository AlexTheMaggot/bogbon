# InternalImports
from . import views
# End InternalImports

# DjangoImports
from django.urls import path
# End DjangoImports


# Config
app_name = 'mainapp'

urlpatterns = [
    # Ru
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news_list'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('about/', views.about, name='about'),
    path('seedlings/', views.seedling_list, name='seedling_list'),
    # End Ru

    # En
    path('en/', views.index, name='index_en'),
    path('en/news/', views.news_list, name='news_list_en'),
    path('en/articles/', views.article_list, name='article_list_en'),
    path('en/articles/<int:id>/', views.article_detail, name='article_detail_en'),
    path('en/shop/', views.product_list, name='product_list_en'),
    path('en/shop/<slug:category_slug>/', views.category_detail, name='category_detail_en'),
    path('en/about/', views.about, name='about_en'),
    path('en/seedlings/', views.seedling_list, name='seedling_list_en'),
    # End En

    # Uz
    path('uz/', views.index, name='index_uz'),
    path('uz/news/', views.news_list, name='news_list_uz'),
    path('uz/articles/', views.article_list, name='article_list_uz'),
    path('uz/articles/<int:id>/', views.article_detail, name='article_detail_uz'),
    path('uz/shop/', views.product_list, name='product_list_uz'),
    path('uz/shop/<slug:category_slug>/', views.category_detail, name='category_detail_uz'),
    path('uz/about/', views.about, name='about_uz'),
    path('uz/seedlings/', views.seedling_list, name='seedling_list_uz'),
    # End Uz
]
# End Config
