from django.shortcuts import render, reverse, HttpResponseRedirect
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
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                b_or_r=data["b_or_r"],
                content=data["content"],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddPostForm()
    return render(request, html, {"form": form})
