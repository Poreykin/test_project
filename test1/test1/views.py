import os
from django.shortcuts import render
from django.views import View
from .crud.models import Article

def react_test(request):
    article = Article.objects.all()[0]
    return render(request, 'index.html', context={'name': article.name,'text': article.text})
