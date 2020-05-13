from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('add-post/', views.addpost, name='add-post')
]
