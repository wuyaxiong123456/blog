from django.shortcuts import render,get_object_or_404
from blog_zhaojianbing.models import *
# Create your views here.

def Post_list(request):
    posts = Post.published.all()
    return render(request,'blog_zhaojianbing/post/list.html',{'posts':posts})

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug = post,status = 'published',publish__year = year,
    publish__month = month,publish__day = day)

    return render(request,'blog_zhaojianbing/post/detail.html',{'post':post})


