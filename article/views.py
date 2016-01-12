# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import article
from datetime import datetime
from django.http import  Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def home(request):
        posts = article.objects.all()
        paginator = Paginator(posts, 2)
        page = request.GET.get('page')
        try :
            post_list = paginator.page(page)
        except PageNotAnInteger :
            post_list = paginator.page(1)
        except EmptyPage :
            post_list = paginator.paginator(paginator.num_pages)
        return render(request, 'home.html', {'post_list' : post_list})

def detail(request,id):
    try:
        post = article.objects.get(id=str(id))
    except article.DoesNotExist:
        raise Http404
    return  render(request,'post.html',{'post':post})
