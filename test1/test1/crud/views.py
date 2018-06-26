from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import CreateForm, UpdateForm

@login_required
def articles_view(request, article_name = None):
    if article_name:
        article = get_object_or_404(Article, name=article_name)
        articles = [{'author': article.author, 'name': article.name, 'text': article.text}]
        full_list = False
    else:
        articles = [{'author': article.author, 'name': article.name, 'text': article.text[:10] + '...'} for article in Article.objects.all()]
        full_list = True

    context = {
        'articles': articles,
        'user': request.user,
        'full_list': full_list,
    }

    return render(request, 'articles_view.html', context)

@login_required
def create_article(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles_view')
    else:
        form = CreateForm()
        return render(request, 'edit_article.html', {'form': form, 'new': True})

@login_required
def update_article(request, article_name = None):
    article = get_object_or_404(Article, name=article_name)

    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            article.name = form.cleaned_data['name']
            article.text = form.cleaned_data['text']
            article.save()
            return redirect('articles_view', article_name=article_name)
    else:
        form = CreateForm(initial={'name': article.name, 'text': article.text})
        return render(request, 'edit_article.html', {'form': form, 'new': False, 'article': article})

@login_required
def delete_article(request, article_name = None):
    article = get_object_or_404(Article, name=article_name)
    article.delete()
        
    return redirect('articles_view')

