from django.shortcuts import render, redirect
from .models import Article, Category
from django.db.models import Count

# Create your views here.

def info(request):
    return render(request, 'info.html')

def project(request):
    return render(request, 'project.html')


def blog(request):
    articles = Article.objects.all()
    categories = Category.objects.annotate(num_posts=Count('article'))
    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'blog.html', context)

def new(request):
    if request.method == 'POST':
        category_id = None  # 기본값으로 None 설정

        if 'category' in request.POST:
            category_id = request.POST['category']

        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category_id=category_id,
        )
        return redirect('blog')

    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'new.html', context)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    category = article.category
    context = {
        'article': article,
        'category': category,
        'created_date': article.created_date,
    }

    return render(request, 'detail.html', context)

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(category_id=category_id)
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'category.html', context)



