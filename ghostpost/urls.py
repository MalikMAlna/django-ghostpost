from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='homepage'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('add-post/', views.addpost, name='add-post'),
    path('up-vote/<int:post_id>/', views.upvoteview),
    path('down-vote/<int:post_id>/', views.downvoteview),
    path('delete/<int:post_id>/', views.deletepost, name='delete-post')
]
