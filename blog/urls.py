from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    re_path(r'ˆpost/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    url(r'ˆpost/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    re_path(r'ˆpost/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'ˆpost/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'ˆpost.(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'ˆpost.(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'ˆpost.(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]
