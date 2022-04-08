from unicodedata import name
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',main_views.register,name='register'),
  path('profile/',main_views.profile,name='profile'),
  path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html'),name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'auth/logout.html'),name='logout'),
  path('index/',main_views.index,name='index'),
  path('update/',main_views.update_profile,name='update_profile'),
  path('others/<int:pk>',main_views.others_profile,name='others_profile'),
  # re_path(r'^comment/(<image_id>\d+)$',main_views.commenting,name='commenting'),
  # re_path(r'^likes/(<image_id>\d+)$',main_views.likes,name='likes'),
  # re_path(r'^search/$',main_views.search,name='search'),
  path('post/',main_views.post,name='post'),
  # re_path(r'^follow/(<user_id>\d+)$',main_views.follow,name='follow'),
  # re_path(r'^unfollow/(<user_id>\d+)$',main_views.unfollow,name='unfollow'),
  # re_path(r'^delete/(<image_id>\d+)$',main_views.delete,name='delete'),
  # re_path(r'^deleteaccount/$',main_views.deleteaccount,name='deleteaccount'),
  # re_path(r'^comment/(<image_id>\d+)$',main_views.commenting,name='commenting'),
  path('allcomments/<str:id>/',main_views.allcomments,name='allcomments'),
  path('comment/<str:id>/',main_views.commenting,name='commenting'),
  path('search/',main_views.search,name='search'),
  path('delete/<str:id>/',main_views.delete,name='delete'),
  path('likes/<str:id>/',main_views.likes,name='likes'),
  path('follow/<str:id>/',main_views.follow,name='follow'),
  path('unfollow/<str:id>/',main_views.unfollow,name='unfollow'),
  path('deleteaccount/<str:id>/',main_views.deleteaccount,name='deleteaccount'),
]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )

