from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from article.models import Article, Comment

from article.forms import ArticleForm


def article(request):
    articles = Article.objects.all()
    itemList = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemList.append(items)
    context = {'itemList': itemList}
    return render(request, 'article/article.html', context)


def articleCreate(request):
    template = 'article/articleCreateUpdate.html'
    # if request is GET, to write article page
    if request.method == 'GET':
        articleForm = ArticleForm()
        print("articleCreate:GET")
        return render(request, template, {'articleForm': articleForm})
    # if request is POST
    articleForm = ArticleForm(request.POST)
    print("articleCreate:POST")
    # data is invalid, save error data
    if not articleForm.is_valid():
        print("data invalid")
        return render(request, template, {'articleForm': articleForm})
    # data is valid, insert data to database
    articleForm.save()
    # return article(request)
    messages.success(request, '文章以新增')
    return redirect('article:article')


def articleRead(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    context = {
        'article': article,
        'comments': Comment.objects.filter(article=article)
    }
    return render(request, 'article/articleRead.html', context)


def articleUpdate(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=article)
        return render(request, template, {'articleForm': articleForm})

    # POST
    articleForm = ArticleForm(request.POST, instance=article)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm': articleForm})
    articleForm.save()
    messages.success(request, '文章已修改')
    return redirect('article:articleRead', articleId=articleId)


def articleDelete(request, articleId):
    if request.method == 'GET':
        return article(request)
    # POST
    article = get_object_or_404(Article, id=articleId)
    article.delete()
    messages.success(request, '文章已刪除')
    return redirect('article:article')


def articleSearch(request):
    searchTerm = request.GET.get('searchTerm')
    # note that __icontains is double _
    # "OR":we can use model Q to search OR condition
    articles = Article.objects.filter(Q(title__icontains=searchTerm) | Q(content__icontains=searchTerm))
    context = {
        'articles': articles,
        'searchTerm': searchTerm}
    return render(request, 'article/articleSearch.html', context)
