from django.shortcuts import render, HttpResponse
from .models import Posts
from django.shortcuts import render, get_object_or_404, Http404, redirect
import datetime
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    posts = Posts.objects.all()

    return render(request, 'index.html', {'posts':posts})

def posts(request, id):
    try:
        posts = Posts.objects.get(id=id)
    except Posts.DoesNotExist:
        raise Http404
    return render(request, 'postlist.html', {'posts': posts})

def add(request, id):
    posts = get_object_or_404(Posts, id=id)
    if request.method == 'POST':       # whatever posted using template will be saved here
        title = request.POST['title']
        slug = request.POST['slug']
        tagline = request.POST['tagline']
        content = request.POST['content']

        post = Posts.objects.create(    # Todo-Used to create a new post from post method
            title = title,
            slug = slug,
            tagline = tagline,
            content = content,
        )
        return redirect('/blog')           #redirected with updation of data
    return render(request, 'newtitle.html', {'posts':posts})          # return object of Posts