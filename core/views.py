
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm


def home_page(request):
    return render(
        request,
        "core/index.html"
    )

def post_list(request):
    posts = Post.objects.all().order_by("-created_date")

    return render(
        request,
        "core/post_list.html",
        {"posts": posts}
    )


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save() # Sparar i databasen
            return redirect("post_list")
    else:
        form = PostForm()

    return render(
        request,
        "core/post_form.html",
        {"form": form}
    )


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.last_edited_date = timezone.now()
            edited_post.save()

            return redirect("post_list")
    else:
        form = PostForm(instance=post) # Fyller formuläret med posten

    return render(
        request,
        "core/post_form.html",
        {
            "form": form,
            "post": post,
        },
    )


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(
        request,
        "core/post_confirm_delete.html",
        {"post": post},
    )
