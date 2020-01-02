from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # return HttpResponse('首页通知书')

    return render(request,'motangtest/index.html')

from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'motangtest/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'motangtest/post/detail.html', {'post': post})