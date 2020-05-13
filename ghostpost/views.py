from django.shortcuts import render
# from .models import Post
from .forms import AddPostForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


def addpost(request):
    html = 'genericform.html'

    if request.method == "POST":
        form = AddPostForm(request.POST)
    form = AddPostForm()
    return render(request, html, {"form": form})
