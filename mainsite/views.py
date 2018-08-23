from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}: ".format(str(count)) + str(post) + "<br>")
        post_lists.append("<small>" + str(post.body.encode('utf-8'))+"</small><br><br>")
    return HttpResponse(post_lists)

def Test(request):
    posts = Post.objects.all()
    now = datetime.now()
    #post_lists = list()
    #for count, post in enumerate(posts):
    #    post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    #    post_lists.append("<small>" + str(post.body.encode('utf-8'))+"</small><br><br>")
    return render(request, 'index.html', locals())

def Test2(request):
    posts = Post.objects.all()
    now = datetime.now()
    #post_lists = list()
    #for count, post in enumerate(posts):
    #    post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    #    post_lists.append("<small>" + str(post.body.encode('utf-8'))+"</small><br><br>")
    return render(request, 'index2.html', locals())

def showpost(request, slug):
    try:
       post = Post.objects.get(slug = slug)
       now = datetime.now()
       if post != None:
          return render(request, 'post.html', locals())
    except:
          return redirect('/')
