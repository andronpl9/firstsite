from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('test', views.test, name = "test"),
    path('test2', views.test2, name = "test2"),
    path('', views.start, name = "start"),
    path('postlist', views.post_list, name = "post_list"),
    path('post/<int:pk>/', views.post_detail, name = "post_detail"),
    path('newpost', views.new_post, name = "post_new"),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
