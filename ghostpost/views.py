from django.shortcuts import render
# from .models import Post
from .forms import AddPost
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


def addpost(request):
    html = 'genericform.html'
    form = AddPost()
    return render(request, html, {"form": form})
