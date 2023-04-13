from django.shortcuts import render, redirect
from .models import Article, Category, Comment, Todo
from django.db.models import Count

# Create your views here.

def info(request):
    return render(request, 'info.html')

def project(request):
    return render(request, 'project.html')

def todolist(request):
    return render(request, 'todolist.html')



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
    article = Article.objects.get(id = article_id)
    comments = Comment.objects.filter(parent_comment = None)
    recomments = Comment.objects.exclude(parent_comment = None).filter(article = article)

    return render(request, 'detail.html', {'article': article, 'comments': comments, 'recomments': recomments})

def delete_comment(request, article_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('detail', article_id)

def create_comment(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content,
        )
        return redirect('detail', article_id)
    return render(request, 'detail.html', {'article': article})

def create_recomment(request, article_id, comment_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        comment = Comment.objects.get(id = comment_id)
        content = request.POST['re_content']
        Comment.objects.create(
            article = article,
            content = content,
            parent_comment = comment
        )
        return redirect('detail', article_id)
    return render(request, 'detail.html', {'article': article})

# def detail(request, article_id):
#     article = Article.objects.get(id=article_id)
#     category = article.category
#     context = {
#         'article': article,
#         'category': category,
#         'created_date': article.created_date,
#     }

#     if request.method == 'POST':
#         content = request.POST['content']
#         Comment.objects.create(
#             article=article,
#             content=content,
#         )
#         return redirect('detail', article_id)

#     return render(request, 'detail.html', context)


def edit(request, article_id):
   article = Article.objects.get(id=article_id)


   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Article.objects.filter(id=article_id).update(
           title=title,
           content=content
       )
       return redirect('detail', article_id)


   return render(request, 'edit.html', {'article':article})




def delete(request, article_id):
   article = Article.objects.get(id=article_id)
   article.delete()



def category(request, category_id):
    category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(category_id=category_id)
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'category.html', context)



def todohome(request):
    Todos = Todo.objects.all()
    return render(request, 'todohome.html', {'Todos': Todos})

def todocreate(request):
    if request.method == "POST":
        new_Todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            end_date = request.POST['end_date']
        )
        return redirect('todohome')
    return render(request, 'todocreate.html')

def tododetail(request, tododetail_pk):
    Todos = Todo.objects.filter(pk=tododetail_pk)
    return render(request, 'tododetail.html', {'Todos': Todos})

def todoupdate(request, tododetail_pk):
    Todos = Todo.objects.filter(pk=tododetail_pk)
    if request.method == "POST":
        Todo.objects.filter(pk=tododetail_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            end_date = request.POST['end_date']
        )
        return redirect('todohome')
    return render(request, 'todoupdate.html', {'Todos': Todos})   

def tododelete(request, tododetail_pk):
    Todos = Todo.objects.filter(pk=tododetail_pk)
    Todos.delete()
    return redirect('todohome')
