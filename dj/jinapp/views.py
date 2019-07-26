# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Article,Reporter
# Create your views here.
def index(request):
    articles = Article.objects.all()
    rep = Reporter.objects.all()
    return render(request,'home.html',{'articles':articles,'reporter':rep})
#    articles_names = list()
#
#    for article in articles:
#        articles_names.append(article.headline)
#
#    response_html = '<br>'.join(articles_names)
#    return HttpResponse(response_html)

def year_arc(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return HttpResponse(render(request, 'mainwindow.html', context))

def datachange(request):
    try:
        #content=request.GET['chkbox_id']
        content=request.GET.getlist('chkbox_id[]')
    except:
        content=None
    print "content is",content
    idstr=",".join(content)
    print "content str is",idstr
    Article.objects.extra(where=['id IN (' + idstr + ')']).delete()
    new_data = Article.objects.all()
    rep = Reporter.objects.all()
    print type(new_data),"\n",new_data,len(new_data)
    info_list=[]
    for ele in new_data:
        info_list.append({"pub_date":ele.pub_date,"headline":ele.headline,"content":ele.content,"reporter":ele.reporter.full_name,})
    print info_list
    return JsonResponse({"articles":info_list})
    #return render(request,'home.html',{'articles':new_data,'reporter':rep})
def search(request):
    try:
        content=request.GET['content']
    except:
        content=None
    print "content is",content
    art = Article.objects.filter(headline=content)
    if content=="all":
        art = Article.objects.all()
    print art,len(art)
    info_list=[]
    for ele in art:
        info_list.append({"id":ele.id,"pub_date":ele.pub_date,"headline":ele.headline,"content":ele.content,"reporter":ele.reporter.full_name,})
    print info_list
    return JsonResponse({"articles":info_list})

def test(request):
    articles = Article.objects.all()
    rep = Reporter.objects.all()
    return render(request,'jin.html',{'articles':articles,'reporter':rep})
