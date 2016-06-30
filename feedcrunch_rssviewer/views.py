# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login, logout

from feedcrunch.models import Post, FeedUser

from feedgen.feed import FeedGenerator
from .functions import *

# Create your views here.

def index(request, feedname=None):

    if feedname == None or (not FeedUser.objects.filter(username = feedname).exists()):
        return HttpResponseRedirect("/")

    else:
        posts = Post.objects.filter(user = feedname).order_by('-id')
        return render(request, 'index.html', {'posts': posts})


def search(request, feedname=None):

    if feedname == None or (not FeedUser.objects.filter(username = feedname).exists()):
        return HttpResponseRedirect("/")

    else:
        posts = Post.objects.filter(user = feedname).order_by('-id')
        return render(request, 'index.html', {'posts': posts})


def redirect(request, feedname=None, postID=None):
    if postID == None or feedname == None :
        return HttpResponse("Error")
    else:
        post = Post.objects.get(id=postID, user=feedname)
        return HttpResponseRedirect(post.link)

def rss_feed(request, feedname=None):
    if feedname == None:
        return HttpResponse("Error")
    else:
        if Post.objects.count() > 0:
            fg = generateRSS("rss")
            return HttpResponse(fg.rss_str(pretty=True, encoding='UTF-8'), content_type='application/xml')
        else:
            return HttpResponse("No Entries in this feed yet")

def atom_feed(request, feedname=None):
    if feedname == None:
        return HttpResponse("Error")
    else:
        if Post.objects.count() > 0:
            fg = generateRSS("atom")
            return HttpResponse(fg.atom_str(pretty=True, encoding='UTF-8'), content_type='application/xml')
        else:
            return HttpResponse("No Entries in this feed yet")
