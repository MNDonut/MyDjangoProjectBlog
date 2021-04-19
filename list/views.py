from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
import requests

def main(request, slug=''):
    context = {}
    form = PostForm()
    # main page
    if slug == "":
        posts = Post.objects.all()
        context["posts"] = posts
        return render(request, f"list/all.html", context)
    # hyperlink to create page
    elif slug == "create":
        # if i send form
        if request.method == "POST":
            newObj = PostForm(request.POST)
            if newObj.is_valid():
                newObj.save()
                return redirect(main)
        # if it's just opening page
        else:
            context["form"] = form
            return render(request, f"list/form_create.html", context)
    return render(request, f"list/all.html", {})

def post_by_id(request, id):
    obj = Post.get_by_id(id)
    context = {
        'obj': obj
    }
    return render(request, f"list/form_get.html", context)

