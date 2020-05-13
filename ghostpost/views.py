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


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'postdetail.html', {'post': post})


def upvoteview(request, post_id):
    post = Post.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def downvoteview(request, post_id):
    post = Post.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))
