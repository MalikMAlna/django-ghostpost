from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('add-post/', views.addpost, name='add-post'),
    path('post/<int:id>/', views.post_detail, name='post-detail'),
    path('up-vote/<int:post_id>/', views.upvoteview),
    path('down-vote/<int:post_id>/', views.downvoteview),
    path('delete/<int:post_id>/', views.deletepost, name='delete-post')
]
