from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', ViewsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('posts/<slug:post_slug>/', Show_post.as_view(), name='post'),
    path('category/<slug:category_slug>/', PersonCategory.as_view(), name='category'),
]
