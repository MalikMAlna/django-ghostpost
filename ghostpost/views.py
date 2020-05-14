from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .forms import AddPostForm
from .models import Post


# def index(request):
#     posts = Post.objects.all().orderby()
#     return render(request, 'index.html', {"posts": posts})

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'


# def post_detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'postdetail.html', {'post': post})

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'postdetail.html'


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


def upvoteview(request, post_id):
    post = Post.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('post-detail', kwargs={"pk": post_id}))


def downvoteview(request, post_id):
    post = Post.objects.get(id=post_id)
    post.down_vote += -1
    post.save()
    return HttpResponseRedirect(reverse('post-detail', kwargs={"pk": post_id}))


def deletepost(request, post_id=None):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect(reverse('homepage'))
