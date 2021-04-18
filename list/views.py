from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostFrom
from .models import Post
import requests

def main(request, slug=''):
    context = {}

    if slug == "":
        posts = Post.objects.all()
        context["posts"] = posts
        return render(request, f"list/all.html", context)
    elif slug == "create":
        form = PostFrom()
        context["create_form"] = form
        return render(request, f"list/form_create.html", context)
    return render(request, f"list/form_find.html", context)


