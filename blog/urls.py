from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    re_path(r'ˆpost/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    url(r'ˆpost/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
