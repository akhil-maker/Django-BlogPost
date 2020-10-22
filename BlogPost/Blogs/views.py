from django.shortcuts import render, HttpResponse
from .models import Posts
from django.shortcuts import render, get_object_or_404, Http404, redirect
import datetime

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
    if request.method == 'POST':
        title = request.form.get('title')
        tagline = request.form.get('tagline')
        slug = request.form.get('slug')
        content = request.form.get('content')
        date = datetime.now()

        if(id==id+1):
            post = Posts(title=title, slug=slug, content=content, tagline=tagline, date=date)
            Posts.add(post)
            Posts.save()
    return render(request, 'newtitle.html', {'posts':posts})