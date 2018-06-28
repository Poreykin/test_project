from django.shortcuts import render
from django.views import View
from .crud.models import Article

def index(request):
    return render(request, 'index.html')


class ArticlesList(View):
    title = "Articles"
    template = 'articles.html'

    def get(self, request):
        article_text = Article.objects.get(name='aaa').text

        context = {
            'article': article_text,
        }

        return render(request, self.template, context)
