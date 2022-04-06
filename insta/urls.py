from django.urls import path,re_path as url
from django.contrib.auth import views as auth_views
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  # path('',main_views.register,name='register'),
  # path('profile/',main_views.profile,name='profile'),
  # path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html'),name='login'),
  # path('logout/',auth_views.LogoutView.as_view(template_name = 'auth/logout.html'),name='logout'),
  # path('index/',main_views.index,name='index'),
  # path('update/',main_views.update_profile,name='update_profile'),
  # url(r'^likes/(?p<image_id>\d+)$',main_views.likes,name='likes'),
  # url(r'^allcomments/(?p<image_id>\d+)$',main_views.allcomments,name='allcomments'),
  # url(r'^search/$',main_views.search,name='search'),
  # path('post/',main_views.post,name='post'),
  # url(r'^post_profile/(?p<pk>\d+)$',main_views.others_profile,name='others_profile'),
  # url(r'^follow/(?p<user_id>\d+)$',main_views.follow,name='follow'),
  # url(r'^unfollow/(?p<user_id>\d+)$',main_views.unfollow,name='unfollow'),
  # url(r'^delete/(?p<image_id>\d+)$',main_views.delete,name='delete'),
  # url(r'^deleteaccount/$',main_views.deleteaccount,name='deleteaccount'),
  # url(r'^comment/(?p<image_id>\d+)$',main_views.commenting,name='commenting'),

]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )

