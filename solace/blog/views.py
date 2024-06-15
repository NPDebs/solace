from django.shortcuts import render
from blog.models import Post, Comment

# Create view to display a list of all posts
def blog_index(request):
    # Get all posts in the database; arrange in reverse order of date created
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

# Create view to display posts under a specific category
def blog_category(request, category):
    # Get all posts; filter using category passed as argument; sort to display most recent first
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

# Create view to display each post in detail (i.e full post, comment)
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)